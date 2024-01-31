def GCD(a,b):
    if b==0:
        return a
    
    return GCD(b,a%b)


if __name__ == '__main__':
    x, y = list(map(int,input().split()))

    area = x*y
    common_unit = GCD(x,y)
    common_area = pow(common_unit,2)

    total_square = area//common_area

    print(total_square)