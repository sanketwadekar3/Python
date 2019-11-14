class Arithmetic:

    def __init__(self,no1,no2):
        self.value1 = no1
        self.value2 = no2

    def Accept(self):
        self.value1 = int(input("Enter number 1"))
        self.value2 = int(input("Enter number 2"))

    def Addition(self):
        return self.value1 + self.value2

    def Subtraction(self):
        return self.value1 - self.value2

    def Multiplication(self):
        return self.value1 * self.value2

    def Division(self):
        return self.value1/self.value2

def main():
    obj1 = Arithmetic(0.0, 0.0)
    obj2 = Arithmetic(0.0, 0.0)

    obj1.Accept()
    ans = obj1.Addition()
    print("Addition is: ",ans)
    ans = obj1.Subtraction()
    print("Subtraction is: ",ans)
    ans = obj1.Multiplication()
    print("Multiplication is: ",ans)
    ans = obj1.Division()
    print("Division is: ",ans)

    obj2.Accept()
    ans = obj2.Addition()
    print("Addition is: ", ans)
    ans = obj2.Subtraction()
    print("Subtraction is: ", ans)
    ans = obj2.Multiplication()
    print("Multiplication is: ", ans)
    ans = obj2.Division()
    print("Division is: ", ans)

if __name__ =='__main__':
    main()