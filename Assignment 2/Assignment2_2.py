def fun(n):
    for x in range(n):
        for x in range(n):
            print("*",end=" ")
        print()

print("Enter number")
num = int(input())
fun(num)