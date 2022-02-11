import cards_db
from card_library import CardLibrary

card_library_test = CardLibrary(cards_db.cards)
class ATM:
    def __init__(self):
        self.inserted_card = None
        self.accounts = []
        self.selected_acc = None

    def verify_card_num(self, card_num):
        return card_num in cards_db.cards_num_to_pin

    def verify_card_pin(self, card_num, pin):
        if card_num in cards_db.cards_num_to_pin:
            return cards_db.cards_num_to_pin[card_num] == pin
        return False
        
    def insert_card(self, card_num):
        self.inserted_card = card_library_test.get_card(card_num)
    
    def remove_card(self):
        self.inserted_card = None

    def get_inserted_card(self):
        return self.inserted_card

    def get_accounts(self):
        return self.inserted_card.get_accounts()

    def verify_account(self, account_num):
        card_accs = self.inserted_card.get_accounts()
        for acc in card_accs:
            if acc.get_acc_num() == account_num:
                return True
        return False
    
    def select_account(self, account_num):
        for acc in self.inserted_card.get_accounts():
            if acc.get_acc_num() == account_num:
                self.selected_acc = acc
        
    def get_selected_account(self):
        return self.selected_acc