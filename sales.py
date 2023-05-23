from car import Car


class Sales(Car):
    def __init__(self, qty, discount, amount) -> None:
        self.qty = qty
        self.discount = discount
        self.amount = amount

    def computeTotalAmount(self):
        discount_deci = int(self.discount) / 100
        total_amount = int(self.price) * int(self.qty)
        total_discount = total_amount * discount_deci
        total = total_amount - total_discount
        return total

    def computeTotalDiscount(self):
        discount_deci = int(self.discount) / 100
        total_amount = int(self.price) * int(self.qty)
        total_discount = total_amount * discount_deci
        return total_discount
