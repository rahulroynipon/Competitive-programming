def GCD(a,b):
    if b == 0:
        return a
    return GCD(b,a%b)
    

if __name__ == '__main__':
    x,y = list(map(int,input().split()))
    print(GCD(x,y))