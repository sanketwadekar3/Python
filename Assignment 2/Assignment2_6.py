def fun(n):
    a = n
    for x in range(n):
        y = 0
        while y < a:
            print("*", end=" ")
            y = y+1
        a = a-1
        print()

print("Enter Number")
num = int(input())
fun(num)