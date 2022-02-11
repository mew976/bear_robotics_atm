class CardLibrary:
    def __init__(self, cards):
        self.cards = cards
    
    def get_card(self, card_num):
        return self.cards[card_num]
