def fun(n):
    ans = 0
    while n >= 1:
        a = n % 10
        ans = int(ans + a)
        n = n / 10
    return ans

print("Enter number")
num = int(input())
ans1 = fun(num)
print(ans1)