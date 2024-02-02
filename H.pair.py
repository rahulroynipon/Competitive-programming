# Given X and Y as the GCD and LCM of two numbers A and B. Find all possible pairs of (A,B).
# Note: (a, b) and (b, a) are considered as two different pairs.

def GCD(a,b):
    if b==0:
        return a
    return GCD(b,a%b)

def pair(a,b):
    count = 0
    mul = a*b
    for i in range(a,mul):
        if (mul%i==0 and GCD(i,mul//i)==a):
            print(i,mul//i)
            count+=1
    return count

if __name__ == '__main__':
    x,y = map(int,input().split())
    print(pair(x,y))