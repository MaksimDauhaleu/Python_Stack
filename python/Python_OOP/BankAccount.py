class BankAccount:
    def __init__(self, name, password, int_rate, balance):
        self.name = name
        self.password = password
        self.balance = balance
        self.int_rate = int_rate
        # self.yield_interest()

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        self.balance -= amount
        if self.balance <= 0:
            print("Insufficient funds: Charging a $35 fee")
            self.balance -= 35
        return self

    def Display_Account_Info(self):
        print("Balance -", self.balance, "$")
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance *= self.int_rate
        return self


maksim = BankAccount("Maksim Dauhaleu", "MaksimPassword", 2, 500)
dennis = BankAccount("Dennis Lloyd", "DennisPassword", 2, 100)
maksim.deposit(100).yield_interest().Display_Account_Info()
dennis.deposit(1000).deposit(500).withdraw(300).withdraw(300).withdraw(300).withdraw(300).yield_interest().Display_Account_Info()
