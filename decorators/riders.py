from .base_decorator import BaseRiderDecorator

class OdontoRider(BaseRiderDecorator):
    def __init__(self, plan, extra_cost: float = 30.0):
        super().__init__(plan)
        self.extra_cost = extra_cost

    def apply_on_price(self, current_price: float) -> float:
        return current_price + self.extra_cost

    def description(self) -> str:
        return "Cobertura Odontológica"


class QuartoPrivativoRider(BaseRiderDecorator):
    def __init__(self, plan, extra_cost: float = 50.0):
        super().__init__(plan)
        self.extra_cost = extra_cost

    def apply_on_price(self, current_price: float) -> float:
        return current_price + self.extra_cost

    def description(self) -> str:
        return "Quarto Privativo"
