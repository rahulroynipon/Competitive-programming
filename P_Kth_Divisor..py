from math import sqrt

def divisor(num,position):
    store = []
    limit = int(sqrt(num))

    i = 1
    while i<=limit:
        x = num%i
        if x==0:
            y = num//i
            store.append(i)
            store.append(y)
        i+=1
    
    return store


def finder(num,position):
    position-=1
    store = divisor(num,position)
    length = len(store)

    if position>=length:
        return -1
    
    store = sorted(store)

    return store[position]




if __name__ == '__main__':
    num = int(input())
    position = int(input())
    print(finder(num,position))
