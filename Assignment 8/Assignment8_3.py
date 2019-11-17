import threading

def Evenlist(list2):
    evensum = 0
    for i in list2:
        if int(i)%2 == 0:
            evensum = evensum + int(i)
    print("Sum of Even Numbers: ",evensum)
    print(threading.current_thread())

def Oddlist(list2):
    oddsum = 0
    for i in list2:
        if int(i)%2 != 0:
            oddsum = oddsum + int(i)
    print("Sum of Odd Numbers: ",oddsum)
    print(threading.current_thread())

def main():
    input_list = input("Enter list numbers seperated by comma: ")
    list1 = input_list.split(",")

    thread1 = threading.Thread(target=Evenlist, args=(list1,))
    thread2 = threading.Thread(target=Oddlist, args=(list1,))

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

if __name__ == '__main__':
    main()