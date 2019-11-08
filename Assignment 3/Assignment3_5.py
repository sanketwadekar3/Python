from MarvellousNum import *
num = list()
def ListPrime():
    n = int(input("Enter number of elements you want: "))
    for i in range(n):
        no = int(input("Enter number: "))
        prime = ChkPrime(no)
        num.append(prime)
    return sum(num)

if __name__=='__main__':
    ans = ListPrime()
    print(ans)
