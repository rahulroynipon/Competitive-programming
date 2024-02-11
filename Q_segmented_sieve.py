from math import isqrt

def segmented_sieve(lower, upper):
    limit = upper - lower + 1
    sieve = [True] * limit

    for i in range(2, isqrt(upper) + 1):
        for j in range(max(i * i, (lower + i - 1) // i * i), upper + 1, i):
            sieve[j - lower] = False
    
    return [i + lower for i in range(limit) if sieve[i]]

if __name__ == '__main__':
    lower, upper = map(int, input().split())
    print(*segmented_sieve(lower, upper))
