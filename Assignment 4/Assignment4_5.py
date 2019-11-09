from functools import *
def ChkNo(no):
    return((no==2 or no==3 or no==5 or no==7) or no%2!=0 and (no%3!=0 and no%5!=0 and no%7!=0))

def Increase(no):
    return no*2

def Max(a,b):
    return max(a,b)

arr = list()

num = int(input("Enter number of elements you want: "))
for i in range(num):
    no = int(input("Enter number: "))
    arr.append(no)

sortedArr = list(filter(ChkNo,arr))
print("Data after filter: ",sortedArr)

incArr = list(map(Increase,sortedArr))
print("Data after map: ",incArr)

mul = reduce(Max,incArr)
print("Output of reduce: ",mul)