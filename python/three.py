"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

def is_prime(n):
    """returns true if n is prime"""
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for x in xrange(3, int(n**0.5)+1, 2):
        if n % x == 0:
            return False
    return True
    
def largest_prime_factor(n):
    """finds the largest prime factor"""
    for x in xrange(int(n**0.5)+1, 3, -2):
        if n % x == 0 and is_prime(x):
            return x
    return n #itself is prime
    
if __name__=="__main__":
    print largest_prime_factor(600851475143)