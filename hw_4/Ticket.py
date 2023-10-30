class Ticket:

    def __init__(self):
        self.price = None
        self.place = None
        self.root_number = None
        self.date_time = None
        self.isValid = None

    def get_price(self):
        return self.price

    def set_price(self, price):
        self.price = price

    def get_place(self):
        return self.place

    def set_place(self, place):
        self.place = place

