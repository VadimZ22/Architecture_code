from Ticket import Ticket
from CashProvider import CashProvider

class Customer():
    def __init__(self):
        self.id = None
        self.name = None
        self.cash_provider = None
        self.tickets = []

    def get_name(self, ):
        return self.name

    def set_name(self, name: str):
        self.name = name

    def set_card(self, number: int):
        self.card_num = number

    def get_card(self):
        return self.card_num

    def buy_ticket(self, ticket: Ticket):
        self.tickets.append(ticket)



