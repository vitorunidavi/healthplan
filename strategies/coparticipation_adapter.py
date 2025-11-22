class CoparticipationAdapter:
    def __init__(self, engine):
        self.engine = engine

    def calculate(self, base_price, age, usage=None):
        if usage is None:
            usage = 0
        return self.calculate_coparticipation(base_price, usage)

    def calculate_coparticipation(self, base_price, usage):
        # Criar classes compatíveis com o strategy
        class DummyUsage:
            def __init__(self, amount):
                self.amount = amount   # <-- AGORA TEM amount

        class DummyCustomer:
            def __init__(self, usage):
                self.age = 0
                self.usage = [DummyUsage(usage)]

        c = DummyCustomer(usage)
        return self.engine.calculate_price(base_price, c)
