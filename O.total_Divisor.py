# n = 12
# 1,2,3,4,6,12 all the divisor of n
# all have pair
# (1,12) (2,6) (3,4)
from math import sqrt

def divisor(n):

    allDivisor = []
    x = int(sqrt(n))+1
    
    for i in range(1,x):
        if n%i==0:
            x1 = n//i
            allDivisor.append(x1)
            allDivisor.append(i)
    
    return allDivisor
    

if __name__ == '__main__':
    n = int(input())
    x = sorted(divisor(n))
    count = len(x)
    print(f'total divisor: {count}')
    print(*x)