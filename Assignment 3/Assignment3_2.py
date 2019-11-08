num = list()
def fun():
    n = int(input("Enter how many elements you want: "))
    for i in range(n):
        no = int(input("Enter no: "))
        num.append(no)
    return max(num)

if __name__=='__main__':
    ans = fun()
    print(ans)