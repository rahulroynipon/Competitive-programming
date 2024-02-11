from math import isqrt

def segmented_sieve(limit):
    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False

    for i in range(2, isqrt(limit) + 1):
        if sieve[i]:
            for j in range(i * i, limit + 1, i):
                sieve[j] = False

    return [i for i in range(limit + 1) if sieve[i]]

def all_prime(nth):
    # Estimate an upper bound based on nth prime
    limit = max(10**3, nth * (int(nth * (math.log(nth) + math.log(math.log(nth))))))

    primes = segmented_sieve(limit)
    return primes[nth - 1]

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        print(all_prime(n))
