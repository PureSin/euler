def getPrimes(n):
    """
        returns all primes from [2,n]
    """
    primes = []
    with open('primes.txt') as f:
        for i in f:
            i = int(i)
            if i <= n:
                primes.append(int(i))
            else:
                return primes
    
def getPrimesRange(l, n):
    primes = []
    with open('primes.txt') as f:
        for i in f:
            i = int(i)
            if i >= l and i <= n :
                primes.append(int(i))
            else:
                return primes