n = int(input("Enter number: "))
fact = n
def main():
    global n,fact
    if(n>1):
        fact = fact*(n-1)
        n = n-1
        main()
    return fact

if __name__=='__main__':
    result = main()
    print(result)