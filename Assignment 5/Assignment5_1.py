n = int(input("Enter number: "))
cnt = 0
def main():
    global cnt
    if(cnt < n):
        print("*",end=" ")
        cnt = cnt + 1
        main()

if __name__=='__main__':
    main()