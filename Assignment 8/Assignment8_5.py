import threading

def seq():
    for i in range(1,51):
        print(i)
    print(threading.current_thread())

def revseq():
    for i in range(50,0,-1):
        print(i)
    print(threading.current_thread())

def main():
    thread1 = threading.Thread(target=seq)
    thread2 = threading.Thread(target=revseq)

    thread1.start()
    if not thread1.isAlive():
        thread2.start()

    thread1.join()
    thread2.join()

if __name__ == '__main__':
    main()