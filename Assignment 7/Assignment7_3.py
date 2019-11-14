import math
class Numbers:
    def __init__(self,value):
        self.value = value

    def ChkPrime(self):
        if(self.value == 2 or self.value == 3 or self.value == 5 or self.value == 7):
            return True
        elif(self.value%2 != 0 and self.value%3 != 0 and self.value%5 != 0 and self.value%7 !=0):
            return True
        else:
            return False

    def ChkPerfect(self):
        temp = math.sqrt(self.value)
        temp1 = int(temp)
        if temp==temp1:
            return True
        else:
            return False

    def Factors(self):
        fact = list()
        for i in range(1, self.value):
            if self.value%i == 0:
                fact.append(i)
        print(fact)
        return fact

    def SumFactors(self,fact):
        sum1 = 0
        length = len(fact)
        for i in range(length):
            sum1 = sum1 + fact[i]
        print(sum1)

def main():
    num = int(input("Enter Number: "))
    obj1 = Numbers(num)
    res = obj1.ChkPrime()
    if res == True:
        print("Prime Number")
    else:
        print("Non-Prime Number")
    res = obj1.ChkPerfect()
    if res == True:
        print("Perfect Number")
    else:
        print("Not a perfect number")
    fact = obj1.Factors()
    obj1.SumFactors(fact)

    num = int(input("Enter Number: "))
    obj2 = Numbers(num)
    res = obj2.ChkPrime()
    if res == True:
        print("Prime Number")
    else:
        print("Non-Prime Number")
    res = obj2.ChkPerfect()
    if res == True:
        print("Perfect Number")
    else:
        print("Not a perfect number")
    fact = obj2.Factors()
    obj2.SumFactors(fact)

if __name__ == '__main__':
    main()