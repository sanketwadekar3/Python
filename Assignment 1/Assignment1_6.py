def fun(n):
    if n==0:
        print("Zero")
    elif n>0:
        print("Positive Number")
    else:
        print("Negative Number")

print("Enter Number")
num = int(input())
fun(num)