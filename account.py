class Account:
    def __init__(self, account_num):
        self.account_num = account_num
        self.balance = 0

    def get_balance(self):
        return self.balance

    def get_acc_num(self):
        return self.account_num
        
    def deposit(self, deposit_amt):
        self.balance += deposit_amt

    def withdraw(self, withdraw_amt):
        if self.balance >= withdraw_amt:
            self.balance -= withdraw_amt
            return True
        else:
            return False
            