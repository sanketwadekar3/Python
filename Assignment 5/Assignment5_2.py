n = int(input("Enter number: "))
cnt = 0
def main():
    global cnt
    if cnt<n:
        cnt = cnt+1
        print(cnt,end=" ")
        main()

if __name__=='__main__':
    main()