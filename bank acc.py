
class Bank:
    auto_accountno = 1

    def __init__(self, name, address,mobno,balance):
        self.name = name
        self.address = address
        self.mobno = mobno
        self.balance = balance
        self.auto_accountno = Bank.auto_accountno
        Bank.auto_accountno = Bank.auto_accountno + 1
        print("Constructor Invoked")

    def withdraw(self, amount):
        if self.balance < amount:
            return -1
        self.balance = self.balance - amount
        return self.balance

    def deposit(self, amount):
        self.balance = self.balance + amount

    def __add__(self, amount):
       self.balance += amount

    def __sub__(self, amount):
        return self.withdraw(amount)


    #def __del__(self):
     #   print("Destructor Invoked")


def main():
    Mah = Bank("Dipty", "Hinjewadi phase 1","7709630588",10000)
    print(Mah.__dict__)
    Mah.withdraw(700)
    print(Mah.__dict__)
    Mah.deposit(1200)
    print(Mah.__dict__)

if __name__ == '__main__':
    main()

