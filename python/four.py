"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

def is_palindrome(s):
    #split in half
    s = str(s)
    if len(s) < 2:
        return True
    if len(s) % 2 == 0:
        first = s[:len(s)/2]
        last = s[len(s)/2:]
    else:
        first = s[:len(s)/2]
        last = s[len(s)/2+1:]
        
    return first[::-1] == last
    
print max(x*y for x in xrange(999,99,-1) for y in xrange(999,99,-1) if is_palindrome(x*y))