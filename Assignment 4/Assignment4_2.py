def fun():
    num1 = int(input("Enter number 1 : "))
    num2 = int(input("Enter number 2 : "))
    fp = lambda value1,value2 : value1*value2
    ret = fp(num1,num2)
    print(ret)

if __name__=='__main__':
    fun()