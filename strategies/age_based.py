from strategies.pricing_strategy import PricingStrategy

class AgeBasedPricing(PricingStrategy):
    def calculate_price(self, base_price: float, customer):
        if customer.age < 18:
            return base_price * 0.7
        elif customer.age > 40:
            return base_price * 1.3
        return base_price
