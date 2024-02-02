def GCD(a,b):
    if b==0:
        return a
    return GCD(b,a%b)
    
if __name__ == '__main__':
    arr = list(map(int,input().split()))
    #The 1st pair GCD
    gcd = GCD(arr[0],arr[1])

    for i in range(2,len(arr)):
        #the 1st pair gcd and next element of arr
        result = GCD(gcd,arr[i]) 
    
    print(result)