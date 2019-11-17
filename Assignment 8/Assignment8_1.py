import threading

def Even():
    even_no = list()
    for i in range(1,11):
        even_no.append(i*2)
    print("Even: ",even_no)
    print(threading.current_thread())

def Odd():
    odd_no = list()
    for i in range(10):
        odd_no.append(i*2+1)
    print("Odd: ",odd_no)
    print(threading.current_thread())

def main():
    thread1 = threading.Thread(target=Even)
    thread2 = threading.Thread(target=Odd)

    thread1.start()
    thread2.start()

if __name__ == '__main__':
    main()