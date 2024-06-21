from math import sqrt
def get_prime_factors(n):
    result=[]
    for i in range(2,n+1):
        if  isPrime(i):
            result.append(i)
    return result
        

def isPrime(n):
    for i in range(2,int(sqrt(n))+1):
        if n%i==0:
            return False
    return True

get_prime_factors(100)