from functools import *
def ChkNo(no):
    return(no%2==0)

def Sqr(no):
    return no*no

def Add(a,b):
    return a+b

arr = list()

num = int(input("Enter number of elements you want: "))
for i in range(num):
    no = int(input("Enter number: "))
    arr.append(no)

sortedArr = list(filter(ChkNo,arr))
print("Data after filter: ",sortedArr)

incArr = list(map(Sqr,sortedArr))
print("Data after map: ",incArr)

mul = reduce(Add,incArr)
print("Output of reduce: ",mul)