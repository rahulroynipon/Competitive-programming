
def binaryExpo(base,power):
    result = 1
    while power>0:
        if power%2==1:
            result*=base
            power-=1
        base*=base
        power = power//2
    
    return result
        

if __name__ == '__main__':
    base,power = map(int,input().split())
    x = binaryExpo(base,power)
    print(x)