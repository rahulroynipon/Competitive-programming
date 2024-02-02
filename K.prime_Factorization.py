
def factor(n):
    ans = []
    for i in range(2,n+1):
        if (n%i==0):
            while (n%i==0):
                n = n/i
                ans.append(i)
    
    return ans


if __name__ == '__main__':
    n  = int(input())
    print(*factor(n))