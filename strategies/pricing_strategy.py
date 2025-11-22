from abc import ABC, abstractmethod


class PricingStrategy(ABC):
    @abstractmethod
    def calculate_price(self, base_price: float, customer):
        pass
