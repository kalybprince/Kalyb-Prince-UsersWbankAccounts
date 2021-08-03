class BankAccount:
    all_accounts = []

    def __init__(self, int_rate=1.01, balance=0): 
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.all_accounts.append([self.int_rate, self.balance])

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if self.balance > 0:
            self.balance -= amount
            return self
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5

    def display_account_info(self):
        return f"Balance: {self.balance}"
        
    def yield_interest(self):
        if self.balance > 0:
            self.balance *= self.int_rate
            return self
        else:
            print("Insufficient funds: Cannot yield interest.")
    
    @classmethod
    def display_all_accounts(cls):
        for i in cls.all_accounts:
            print(i)

class User:
    def __init__(self, name):
        self.name = name
        self.balance = 0
        self.account = BankAccount()

    def make_deposit(self, deposit):
        self.account.balance += deposit

    def make_withdrawal(self, withdrawal):
        self.account.balance -= withdrawal

    def display_user_balance(self):
        return self.account.balance

    def transfer_money(self, payee, amount):
        self.make_withdrawal(amount)
        payee.make_deposit(amount)

account_1 = User('kalyb')
account_2 = User('prince')

