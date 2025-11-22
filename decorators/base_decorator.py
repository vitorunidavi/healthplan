class BaseRiderDecorator:
    def __init__(self, plan):
        self.plan = plan

    def apply_on_price(self, current_price: float) -> float:
        return current_price  # padrão

    def description(self) -> str:
        return "Rider genérico"
