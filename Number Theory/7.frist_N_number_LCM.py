def GCD(a,b):
    if b==0:
        return a
    return GCD(b,a%b)

def LCM(a,b):
    gcd = GCD(a,b)
    return (a*b)//gcd


if __name__ == '__main__':
    n = int(input())
    lcm = 1
    for i in range(2,n+1):
        lcm = LCM(lcm,i)
    print(lcm)


