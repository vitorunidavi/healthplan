from factory.plan_factory import PlanFactory
from domain.plan import Plan

def test_singleton_instance():
    f1 = PlanFactory()
    f2 = PlanFactory()
    assert f1 is f2

def test_create_basic_plan():
    factory = PlanFactory()
    plan = factory.create_plan("basic")
    assert isinstance(plan, Plan)
    assert plan.name == "Basic"

def test_create_premium_plan():
    factory = PlanFactory()
    plan = factory.create_plan("premium")
    assert isinstance(plan, Plan)
    assert plan.name == "Premium"
