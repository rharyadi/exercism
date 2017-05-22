def sieve(n):
    not_prime = 2
    not_primes = set()
    while not_prime <= n:
        i = not_prime
        while i <= n:
            i = i + not_prime
            if i > n:
                break
            not_primes.add(i)
        not_prime = not_prime + 1
    whole = {i for i in range(2,n+1)}
    primes = list(whole - not_primes)
    primes.sort()
    return primes
