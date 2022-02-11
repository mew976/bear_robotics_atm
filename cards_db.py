from card import Card
from account import Account
Account1 = Account("1111")
Account2 = Account("2222")
Account3 = Account("3333")

card1 = Card("1234567890", "1234", [Account1, Account2, Account3]) 
card2 = Card("0987654321", "4321", []) # no accounts

cards_num_to_pin = {
    "1234567890": "1234",
    "0987654321": "4321",
}

cards = {"1234567890": card1, "0987654321": card2}