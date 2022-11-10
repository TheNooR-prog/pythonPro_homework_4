class NegativeValue(Exception):

    def __init__(self, number):
        super().__init__()
        self.number = number

    def __str__(self):
        return "Negative price"

class StudentsLimit(Exception):

    def __init__(self, message):
        super().__init__()
        self.message = message

    def __str__(self):
        return f"{self.message}"
