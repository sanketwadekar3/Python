num = list()
def fun():
    n = int(input("Enter how many elements you want: "))
    for i in range(n):
        no = int(input("Enter number: "))
        num.append(no)
    return min(num)

if __name__=='__main__':
    ans = fun()
    print(ans)