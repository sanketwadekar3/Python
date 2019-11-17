import threading

def Evenfactor(no):
    evensum = 0
    for i in range(1,no):
        if no%i == 0 and i%2 == 0:
            evensum = evensum + i
    print("Sum of Even Factors: ",evensum)
    print(threading.current_thread())

def Oddfactor(no):
    oddsum = 0
    for i in range(1,no):
        if no%i == 0 and i%2 != 0:
            oddsum = oddsum + i
    print("Sum of Odd Fators: ",oddsum)
    print(threading.current_thread())

def main():
    no1 = int(input("Enter Number"))

    thread1 = threading.Thread(target=Evenfactor, args=(no1,))
    thread2 = threading.Thread(target=Oddfactor, args=(no1,))

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    print("Exit from main")

if __name__=='__main__':
    main()