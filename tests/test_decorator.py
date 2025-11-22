from domain.plan import Plan
from decorators.riders import OdontoRider, QuartoPrivativoRider

class DummyStrategy:
    def calculate(self, base_price, age, usage=None):
        return base_price


def test_single_rider():
    plan = Plan(id=1, name="Básico", base_price=100, pricing_strategy=DummyStrategy())
    plan.add_rider(OdontoRider(plan, extra_cost=30))

    final_price = plan.calculate_price(customer_age=30)
    assert final_price == 130


def test_multiple_riders_composition():
    plan = Plan(id=1, name="Básico", base_price=100, pricing_strategy=DummyStrategy())
    plan.add_rider(OdontoRider(plan, extra_cost=30))
    plan.add_rider(QuartoPrivativoRider(plan, extra_cost=50))

    final_price = plan.calculate_price(customer_age=30)
    assert final_price == 180


def test_order_does_not_break_decorator_chain():
    plan = Plan(id=1, name="Básico", base_price=100, pricing_strategy=DummyStrategy())
    plan.add_rider(QuartoPrivativoRider(plan, extra_cost=50))
    plan.add_rider(OdontoRider(plan, extra_cost=30))

    final_price = plan.calculate_price(customer_age=25)
    assert final_price == 180
