def ChkPrime(n):
    if n==2 or n==3 or n==5 or n==7:
        return n
    if n%2!=0 and n%3!=0 and n%5!=0 and n%7!=0:
        return n
    else:
        return 0