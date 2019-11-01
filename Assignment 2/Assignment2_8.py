def fun(n):
    a = 2
    for x in range(1,n+1):
        for y in range(1,a):
            print(y, end=" ")
        a = a+1
        print()

print("Enter Number")
num = int(input())
fun(num)