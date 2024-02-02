def countFactor(n):
    count = 0
    for i in range(2,n+1):
        if (n%i==0):
            count+=1
            while (n%i==0):
                n = n/i
    
    return count


if __name__ == '__main__':
    n = int(input())
    print(countFactor(n))