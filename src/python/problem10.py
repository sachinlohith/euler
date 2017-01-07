'''
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
'''

from util import genPrimes


def solution():
    '''
    Returns:
        sum of all primes below two million
    '''
    primes = [2]
    prime = genPrimes()
    while primes[-1] < 2000000:
        primes.append(next(prime))
    return sum(primes[1:-1])


if __name__ == "__main__":
    print solution()
