from three import is_prime
from primes import getPrimes
"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""
#TODO speed up
def prime_factors(n):
    """returns all prime factors of n"""
    l = {}
    listOfPrimes = getPrimes(n)
    for p in listOfPrimes:
        while n % p == 0:
            n = n / p
            l[p] = l.get(p, 0) + 1
    return l

if __name__=="__main__":
    x = xrange(1,21)
    all_factors = {}
    for i in x:
        factors = prime_factors(i)
        for key in factors.keys():
            if factors[key] > all_factors.get(key, 0):
                all_factors[key] = factors[key]
    num = 1
    for key in all_factors.keys():
        num *= key**all_factors[key]
    print num