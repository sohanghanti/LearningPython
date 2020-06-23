class Bank:

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def __str__(self):
        return f'Account owner {self.owner} has balance {self.balance}'

    def deposit(self, deposit):
        print(str(deposit) + ' deposited in account')
        self.balance = self.balance + deposit

    def withdraw(self, withdraw):
        if withdraw > self.balance:
            print('You do not have sufficient balance')
        else:
            self.balance = self.balance - withdraw
            print('withdrawal ' + str(withdraw) + ' is successful')
            return self.balance


b = Bank('Sohan', 10000)
print(b)

b.deposit(5000)
print(b)

b.withdraw(10000)
print(b)