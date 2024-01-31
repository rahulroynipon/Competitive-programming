from math import sqrt

def allPrime(n_th):
    n = pow(10,5)
    primeStore = [True]*n
    primeStore[0] = primeStore[1] = False
    y = int(sqrt(n))+1

    for i in range(2,y):
        if primeStore[i]:
            for j in range(i*i,n,i):
                primeStore[j] = False
    
    newPrime = []
    for index,value in enumerate(primeStore):
        if value:
            newPrime.append(index)
    
    return newPrime[n_th-1]



if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        print(allPrime(n))

