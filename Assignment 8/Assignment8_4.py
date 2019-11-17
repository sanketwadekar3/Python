import threading
import string

def small(s):
    smallcnt = 0
    for i in s:
        if i.islower():
            smallcnt = smallcnt + 1
    print("Small Count: ",smallcnt)
    print(threading.current_thread())

def capital(s):
    capscnt = 0
    for i in s:
        if i.isupper():
            capscnt = capscnt + 1
    print("Capital Count: ",capscnt)
    print(threading.current_thread())

def digits(s):
    digitcnt = 0
    for i in s:
        if i.isdigit():
            digitcnt = digitcnt + 1
    print("Digit Count: ",digitcnt)
    print(threading.current_thread())

def main():
    s1 = input("Enter String: ")

    thread1 = threading.Thread(target=small, args=(s1,))
    thread2 = threading.Thread(target=capital, args=(s1,))
    thread3 = threading.Thread(target=digits, args=(s1,))

    thread1.start()
    thread2.start()
    thread3.start()

    thread1.join()
    thread2.join()
    thread3.join()

if __name__ == '__main__':
    main()