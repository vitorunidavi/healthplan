class CoparticipationPricing:
    def __init__(self, rate=None, copay_rate=None):
        self.copay_rate = copay_rate if copay_rate is not None else rate

    def calculate_price(self, base_price: float, customer):
        # os testes exigem que customer.usage contenha objetos com atributo "amount"
        total_usage = sum(u.amount for u in customer.usage)
        copay = total_usage * self.copay_rate
        return base_price + copay
