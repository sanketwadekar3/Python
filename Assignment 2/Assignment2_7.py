def fun(n):
    for x in range(1,n+1):
        for y in range(1,n+1):
            print(y, end=" ")
        print()

print("Enter Number")
num = int(input())
fun(num)