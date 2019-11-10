n = int(input("Enter number: "))
sum = 0
def main():
    global n,sum
    if(n>0):
        sum = sum + n%10
        n = int(n/10)
        main()
    return sum

if __name__=='__main__':
    result = main()
    print(result)