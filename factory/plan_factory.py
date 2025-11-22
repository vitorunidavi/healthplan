from domain.plan import Plan
from strategies.age_based import AgeBasedPricing
from strategies.coparticipation import CoparticipationPricing


class PlanFactory:
    """
    Factory Singleton + Factory Method exigido pelos testes.
    """

    _instance = None  # ← necessário para o Singleton

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    # --------------------------------------------------------------------

    def create_plan(self, plan_type: str) -> Plan:
        """
        Método exigido pelo test_factory.py
        Retorna basic / premium conforme string.
        """
        plan_type = plan_type.lower()

        if plan_type == "basic":
            return self.create_basic_plan()
        elif plan_type == "premium":
            return self.create_premium_plan()
        else:
            raise ValueError(f"Tipo de plano desconhecido: {plan_type}")

    # --------------------------------------------------------------------

    @staticmethod
    def create_basic_plan() -> Plan:
        return Plan(
            id=1,
            name="Basic",
            base_price=100,
            quota=500,
            pricing_strategy=AgeBasedPricing()
        )

    @staticmethod
    def create_premium_plan() -> Plan:
        return Plan(
            id=2,
            name="Premium",
            base_price=200,
            quota=1200,
            pricing_strategy=CoparticipationPricing(rate=0.2)
        )

    @staticmethod
    def create_custom_plan(name: str, base_price: float, quota: float, strategy) -> Plan:
        return Plan(
            id=999,
            name=name,
            base_price=base_price,
            quota=quota,
            pricing_strategy=strategy
        )
