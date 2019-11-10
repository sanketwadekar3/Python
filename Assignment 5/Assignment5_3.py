n = int(input("Enter number: "))
cnt = 0
def main():
    global n
    if cnt < n:
        print(n,end=" ")
        n = n-1
        main()

if __name__=='__main__':
    main()