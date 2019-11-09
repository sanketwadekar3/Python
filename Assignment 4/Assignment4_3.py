from functools import *
def ChkNo(no):
    return(no>=70 and no<=90)

def Increase(no):
    return no+10

def Multiply(a,b):
    return a*b

arr = list()

num = int(input("Enter number of elements you want: "))
for i in range(num):
    no = int(input("Enter number: "))
    arr.append(no)

sortedArr = list(filter(ChkNo,arr))
print("Data after filter: ",sortedArr)

incArr = list(map(Increase,sortedArr))
print("Data after map: ",incArr)

mul = reduce(Multiply,incArr)
print("Output of reduce: ",mul)