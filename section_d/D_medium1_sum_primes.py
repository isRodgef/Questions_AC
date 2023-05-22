import math 


def atkin(limit):
    """ Returns a list of prime numbers below the limit """
    results = [2,3]
    sieve = [False] * limit
    for x in range(1, int(math.sqrt(limit))+1):
        for y in range(1, int(math.sqrt(limit))+1):
            n = 4*x* x + y**2
            if n <= limit and (n % 12 == 1 or n % 12 == 5):
                sieve[n] = not sieve[n]
            n = 3*x**2+y**2
            if n <= limit and n % 12 == 7:
                sieve[n] = not sieve[n]
            n = 3*x**2 - y**2
            if x > y and n <= limit and n % 12 == 11:
                sieve[n] = not sieve[n]
    for x in range(5, int(math.sqrt(limit))):
        if sieve[x]:
            for y in range(x**2, limit, x**2):
                sieve[y] = False
    for p in range(5, limit):
        if sieve[p]:
            results.append(p)
    return results

if __name__ == '__main__':
    print(sum(atkin(2000000)))