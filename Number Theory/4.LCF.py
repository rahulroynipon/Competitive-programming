def GCD(a,b):
    if b==0:
        return a
    return GCD(b,a%b)

def LCF(a,b):
    gcd = GCD(a,b)

    # a*b = GCD(a,b)*LCF(a,b)
    return (a*b)//gcd

if __name__ == '__main__':
    x,y = list(map(int,input().split()))
    print(LCF(x,y))