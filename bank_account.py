class BankAccount:
    def __init__(self , owner , balance):
       self.owner = owner
       self.balance = balance
    def deposit(self , amount):
        self.balance += amount
        print(f"{amount} deposit hua balance {self.balance}")
    def withraw(self , amount):
        if amount > self.balance:
            print(f"insufficient balance!")
        else:
            self.balance -= amount
            print(f"{self.owner} ka balance{self.balance}")
    def show(self):
        print(f"{self.owner} ka balance {self.balance} ")


account = BankAccount("Ali" , 5000 )
account.show()
account.deposit(2000)
account.withraw(1000)
account.withraw(10000)


