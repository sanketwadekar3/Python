def fun(n):
    ans = 0
    for x in range(1,n-1):
        if n%x == 0:
            ans = ans + x
    return ans

print("Enter number")
num = int(input())
ans1 = fun(num)
print(ans1)