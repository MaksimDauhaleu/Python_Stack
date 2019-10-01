class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0


    def make_deposit(self, amount):
        self.account_balance += amount


    def make_withdrawal(self, amount):
        self.account_balance -= amount


    def zelle_pay(self, name, amount):
        name.account_balance += amount
        self.account_balance -= amount




Dennis = User("Dennis Lloyd", "dennislloyd@gmail.com")
Maksim = User("Maksim Dauhaleu", "maksimdauhaleu@gmail.com")
Maksim.make_deposit(200)
Maksim.zelle_pay(Dennis, 50)

print(Maksim.name, ", Balance - ", Maksim.account_balance, "$")
print(Dennis.name, ", Balance - ", Dennis.account_balance, "$")