def fun(n):
    if n == 2 or n == 3 or n == 5 or n == 7:
        print("It is Prime Number")
    elif n % 2 != 0 and n % 3 != 0 and n % 5 != 0 and n % 7 != 0:
        print("It is Prime Number")
    else:
        print("It is not a Prime Number")

print("Enter Number")
num = int(input())
fun(num)