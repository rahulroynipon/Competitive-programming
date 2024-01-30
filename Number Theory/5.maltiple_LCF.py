def GCD(a,b):
    if b==0:
        return a
    return GCD(b,a%b)

def LCF(a,b):
    gcd = GCD(a,b)
    return (a*b)//gcd


if __name__ == '__main__':
    arr = list(map(int,input().split()))

    num1 = arr[0]
    num2 = arr[1]

    lcf = LCF(num1,num2)
    for i in range(2,len(arr)):
        lcf = LCF(lcf,arr[i])
    
    print(lcf)