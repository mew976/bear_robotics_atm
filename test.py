import unittest

from atm import ATM
import cards_db

card_num1_good = "1234567890"
card_num2_good = "0987654321"
card_num_bad = "3123131789"

card_pin1_good = "1234"
card_pin2_good = "4321"
card_pin_bad = "3456"

account1_good = "1111"
account2_good = "2222"
account3_good = "3333"
account_bad = "4444"

class Test(unittest.TestCase):
    def test_verify_card_num(self):
        atm = ATM()
        self.assertTrue(atm.verify_card_num(card_num1_good))
        self.assertFalse(atm.verify_card_num(card_num_bad))
    
    def test_verify_card_pin(self):
        atm = ATM()
        self.assertTrue(atm.verify_card_pin(card_num1_good, card_pin1_good))
        self.assertFalse(atm.verify_card_pin(card_num1_good, card_pin2_good))
        self.assertFalse(atm.verify_card_pin(card_num_bad, card_pin_bad))

    def test_insert_remove_card(self):
        atm = ATM()
        card = atm.insert_card(card_num1_good)
        self.assertEqual(atm.get_inserted_card().get_number(), card_num1_good)
        self.assertNotEqual(atm.get_inserted_card().get_number(), card_num2_good)

        atm.remove_card()
        self.assertIsNone(atm.get_inserted_card())


    def test_select_account(self):
        atm = ATM()
        card = atm.insert_card(card_num1_good)
        self.assertFalse(atm.verify_account(account_bad))
        self.assertTrue(atm.verify_account(account1_good))

        atm.select_account(account_bad)
        self.assertIsNone(atm.get_selected_account())
        atm.select_account(account1_good)
        self.assertEqual(atm.get_selected_account().get_acc_num(), account1_good)

    def test_view_balance(self):
        atm = ATM()
        card = atm.insert_card(card_num1_good)
        atm.select_account(account1_good)
        self.assertEqual(atm.get_selected_account().get_balance(), 0)

    def test_deposit(self):
        atm = ATM()
        card = atm.insert_card(card_num1_good)
        atm.select_account(account2_good)
        atm.get_selected_account().deposit(5)
        self.assertEqual(atm.get_selected_account().get_balance(), 5)
        atm.get_selected_account().deposit(50)
        self.assertEqual(atm.get_selected_account().get_balance(), 55)

    def test_withdraw(self):
        atm = ATM()
        card = atm.insert_card(card_num1_good)
        atm.select_account(account3_good)
        self.assertFalse(atm.get_selected_account().withdraw(5))
        atm.get_selected_account().deposit(50)
        atm.get_selected_account().withdraw(25)
        self.assertEqual(atm.get_selected_account().get_balance(), 25)
        atm.get_selected_account().deposit(10)
        self.assertEqual(atm.get_selected_account().get_balance(), 35)
        atm.get_selected_account().withdraw(20)
        self.assertEqual(atm.get_selected_account().get_balance(), 15)



unittest.main()