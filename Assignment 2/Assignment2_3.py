def fun(n):
    ans = n
    for x in range(1,n):
        ans = ans*x
    return ans

print("Enter number")
num = int(input())
ans1 = fun(num)
print(ans1)