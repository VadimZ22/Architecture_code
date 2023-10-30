from Customer import Customer
class CashProvider():

    def __init__(self, card_num):
        self.card_num = card_num
        self.autorization = False

    def set_card_num(self, num):
        self.card_num = num

    def get_card_num(self):
        return self.card_num

    def autorizations(self, customer: Customer):
        self.autorization = True