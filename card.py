class Card:
    def __init__(self, card_num, card_pin, accounts):
        self.number = card_num 
        self.pin = card_pin
        self.accounts = accounts # list of accounts associated to this card

    def get_number(self):
        return self.number
    
    def get_accounts(self):
        return self.accounts