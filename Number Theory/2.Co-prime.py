def GCD(a,b):
    if b==0:
        return a
    return GCD(b,a%b)

if __name__ == '__main__':
    x, y = list(map(int,input().split()))
    

    #Co-prime: Two numbers A and B are said to be Co-Prime or mutually prime 
    #if the Greatest Common Divisor of them is 1.
    ans = GCD(x,y)
    print(f'{x} and {y} are co-prime' if ans==1 else 'NO')
