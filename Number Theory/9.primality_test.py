from math import sqrt

def prime(n):
    if n<2:
        return False
    root = int(sqrt(n))+1
    for i in range(2,root):
        if n%i==0:
            return False
    return True


if __name__ == '__main__':
    n = int(input())
    print('prime' if prime(n) else 'not prime')