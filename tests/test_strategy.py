from strategies.age_based import AgeBasedPricing
from strategies.coparticipation import CoparticipationPricing


class DummyCustomer:
    def __init__(self, age, usage=None):
        self.age = age
        self.usage = usage or []


class DummyUsage:
    def __init__(self, amount):
        self.amount = amount


def test_age_based_under_18():
    strategy = AgeBasedPricing()
    c = DummyCustomer(age=10)
    assert strategy.calculate_price(100, c) == 70


def test_age_based_adult():
    strategy = AgeBasedPricing()
    c = DummyCustomer(age=30)
    assert strategy.calculate_price(100, c) == 100


def test_age_based_over_40():
    strategy = AgeBasedPricing()
    c = DummyCustomer(age=50)
    assert strategy.calculate_price(100, c) == 130


def test_coparticipation():
    strategy = CoparticipationPricing(copay_rate=0.2)
    c = DummyCustomer(age=30, usage=[DummyUsage(50), DummyUsage(50)])
    assert strategy.calculate_price(100, c) == 120
