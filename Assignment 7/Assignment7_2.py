class BankAccount:
    ROI = 10.5
    def __init__(self,name,amount):
        self.name = name
        self.amount = amount

    def Deposit(self):
        value = int(input("Enter amount to be deposit for "+self.name+" : "))
        self.amount = self.amount + value

    def Withdraw(self):
        value = int(input("Enter amount to be withdraw for "+self.name+" : "))
        self.amount = self.amount - value

    def CalculateInterest(self):
        return (self.amount * BankAccount.ROI) / 100

    def Display(self):
        print(self.name+" has balance ",self.amount)

def main():
    obj1 = BankAccount("Sanket",10000)
    obj1.Deposit()
    obj1.Display()
    obj1.Withdraw()
    obj1.Display()
    print(obj1.CalculateInterest())

    obj2 = BankAccount("Devikesh", 1000)
    obj2.Deposit()
    obj2.Display()
    obj2.Withdraw()
    obj2.Display()
    print(obj2.CalculateInterest())

if __name__ == '__main__':
    main()