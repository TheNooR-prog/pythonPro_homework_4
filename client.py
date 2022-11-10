class Client:

    def __init__(self, surname, name, middle_name, mobile):
        self.surname = surname
        self.name = name
        self.middle_name = middle_name
        self.mobile = mobile

    def __str__(self):
        return f"Client: {self.surname} {self.name[0:1]}.{self.middle_name[0:1]}.\nPhone: {self.mobile}"
