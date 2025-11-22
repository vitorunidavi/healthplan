from domain.plan import Plan
from observers.notifications import QuotaObserver
from domain.usage import Usage

class DummyStrategy:
    def calculate(self, base_price, age, usage=None):
        return base_price

def test_quota_notifications():
    plan = Plan(id=1, name="Premium", base_price=100, quota=100, pricing_strategy=DummyStrategy())

    observer = QuotaObserver()
    plan.attach(observer)

    plan.apply_usage(Usage(amount=80, description="Exame"))  # ≥80% → quota_high
    plan.apply_usage(Usage(amount=30, description="Consulta"))  # ≥100% → quota_exceeded

    assert len(plan.usage_history) == 2
