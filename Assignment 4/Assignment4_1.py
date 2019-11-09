def fun():
    num = int(input("Enter number: "))
    fp = lambda val : val*val
    ret = fp(num)
    print(ret)

if __name__=='__main__':
    fun()