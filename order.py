import item

class Order():

    def __init__(self, title, client):
        self.title = title
        self.client = client
        self.items = []

    def add_items(self, itemm):
        if isinstance(itemm, item.Item):
            self.items.append(itemm)

    def total(self):
        summa = 0
        for i in self.items:
            summa += i.price
        return f"Total: {summa} UAH"

    def __str__(self):
        return f"{self.title}\n{self.client}\n" + "\n".join(map(str, self.items))
