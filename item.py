import custom_extantions

class Item:

    def __init__(self, description, price, l, w, h):
        if int(price) <= 0:
            raise custom_extantions.NegativeValue(price)
        self.price = price
        self.description = description
        self.l = l
        self.h = h
        self.w = w

    def __str__(self):
        return f"Item: {self.description}\nPrice: {self.price} UAH\nDimentions: {self.l}x{self.w}x{self.h}cm"