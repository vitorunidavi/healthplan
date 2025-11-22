from __future__ import annotations
from typing import List, Protocol, Optional
from dataclasses import dataclass, field
from .usage import Usage
from infra.logger_singleton import Logger


# Interface mínima para PricingStrategy (Strategy)
class PricingStrategy(Protocol):
    def calculate(self, base_price: float, customer_age: int, usage: Optional[Usage] = None) -> float:
        ...


@dataclass
class Plan:
    id: int
    name: str
    base_price: float
    quota: float = 0.0
    pricing_strategy: Optional[PricingStrategy] = None
    riders: List[object] = field(default_factory=list)
    observers: List[object] = field(default_factory=list)
    usage_history: List[Usage] = field(default_factory=list)

    def attach(self, observer: object) -> None:
        if observer not in self.observers:
            self.observers.append(observer)

    def detach(self, observer: object) -> None:
        if observer in self.observers:
            self.observers.remove(observer)

    def notify(self, event: str, **data) -> None:
        logger = Logger()
        for o in self.observers:
            try:
                o.update(self, event, **data)
            except Exception as e:
                logger.warn(f"Observer raised error: {e}")

    def apply_usage(self, usage: Usage) -> None:
        self.usage_history.append(usage)
        total_used = sum(u.amount for u in self.usage_history)
        logger = Logger()
        logger.info(f"Uso registrado: {usage.description} R${usage.amount:.2f}. Total usado: R${total_used:.2f}")

        if self.quota > 0:
            pct = total_used / self.quota
            if pct >= 1.0:
                self.notify('quota_exceeded', total=total_used)
            elif pct >= 0.8:
                self.notify('quota_high', total=total_used)

    def calculate_price(self, customer_age: int, usage: Optional[Usage] = None) -> float:
        logger = Logger()
        logger.info("Calculando preço do plano...")

        price = self.base_price

        if self.pricing_strategy is not None:
            price = self.pricing_strategy.calculate(self.base_price, customer_age, usage)

        for r in self.riders:
            logger.info(f"Aplicando rider: {r.__class__.__name__}")
            if hasattr(r, 'apply_on_price'):
                price = r.apply_on_price(price)

        return price

    def add_rider(self, rider: object) -> None:
        self.riders.append(rider)
