class Account():
    def __init__(self, n, b, p):
        self.number = n
        self.balance = b
        self.password = p
    def deposit(self, amountToDepo, password):
        if password != self.password:
            print("Sorry, incorrect password. ")
            return None
        if amountToDepo < 0:
            print("You cannot deposit a negative amount. ")
            return None
        self.balance += amountToDepo
        return self.balance

    def show(self):
        print(self.number)
        print(self.balance)

def main():
    alice = Account("0001", 10000.50, "bsu")
    bob = Account("0002", 100, "iu")
    bob.show()
    alice.deposit(200, "bsu")
    alice.show()

main()
