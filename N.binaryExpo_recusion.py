# Binary Exponention
# slove by recusion method
# pow(10,9)
# 10*pow(10,8)
# 10*pow(10,4)*pow(10,4)
# 10*pow(10,2)*pow(10,2)*pow(10,2)*pow(10,2)
# 10*pow(10,1)*pow(10,1)*pow(10,1)*pow(10,1)*pow(10,1)*pow(10,1)*pow(10,1)*pow(10,1)
# 10*10*pow(10,0)*10*pow(10,0)*10*pow(10,0)*10*pow(10,0)*10*pow(10,0)*10*pow(10,0)*10*pow(10,0)*10*pow(10,0)

def binaryExpo(base,power):
    if power==0:
        return 1
    if power%2==1:
        power-=1
        temp = binaryExpo(base,power)
        return base*temp
    
    power = power//2
    result = binaryExpo(base,power)
    print(base,power,result)
    return result*result

if __name__ == '__main__':
    base,power = map(int,input().split())
    x = binaryExpo(base,power)
    print(x)