def fun(n):
    ans = 1
    while n > 10:
        n = n / 10
        ans = ans + 1
    return ans

print("Enter number")
num = int(input())
ans1 = fun(num)
print(ans1)