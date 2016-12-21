'''
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13,
we can see that the 6th prime is 13.

What is the 10,001st prime number?
'''

from util import divisibleByAnyInList


def nextPrime(primes):
    count = primes[-1]+2
    while count < primes[-1]*2:
        if not divisibleByAnyInList(count, primes):
            return count
        count += 2


def solution():
    primes = [2, 3]
    count = 2
    while count < 10001:
        primes.append(nextPrime(primes))
        count += 1
    return primes[-1]


if __name__ == "__main__":
    print solution()
