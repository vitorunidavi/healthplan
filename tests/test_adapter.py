from strategies.coparticipation_adapter import CoparticipationAdapter
from strategies.coparticipation import CoparticipationPricing

def test_adapter_basic_behavior():
    engine = CoparticipationPricing(rate=0.2)
    adapter = CoparticipationAdapter(engine)

    result = adapter.calculate(base_price=100, age=25, usage=10)

    assert result == 100 + (10 * 0.2)
