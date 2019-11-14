class Demo:
    Value = 5
    def __init__(self,no1,no2):
        self.number1 = no1
        self.number2 = no2
    def fun(self):
        print(self.number1)
    def gun(self):
        print(self.number2)

def main():
    obj1 = Demo(11,21)
    obj2 = Demo(51,101)
    obj1.fun()
    obj2.fun()
    obj1.gun()
    obj2.gun()

if __name__ == '__main__':
    main()