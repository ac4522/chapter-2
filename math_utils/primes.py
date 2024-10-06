from math import sqrt, floor
def isprime(n):
    if n<2:
        return False
    elif n==2 or n==3:
        return True
    else:
        for i in range(2,floor(sqrt(n))+1):
            if n%i==0:
                return False
                break
            else:
                return True