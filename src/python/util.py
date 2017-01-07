'''
Handy functions to use in solving other problems
'''


def divisibleByWholeList(number, factors):
    return all(map(lambda x: number % x == 0, factors))


def divisibleByAnyInList(number, factors):
    return any(map(lambda x: number % x == 0, factors))


def genPrimes():
    '''
    Generate an infinte sequence of primes
    '''

    witnessMap = {}
    composite = 2
    while True:
        if composite not in witnessMap:
            yield composite
            witnessMap[composite*composite] = [composite]
        else:
            for prime in witnessMap[composite]:
                witnessMap.setdefault(prime + composite, []).append(prime)
            del witnessMap[composite]
        composite += 1

def divisorGenerator(n):
    '''
    Generate divisors for a given number
    '''

    import math
    large_divisors = []
    for i in xrange(1, int(math.sqrt(n) + 1)):
        if n % i == 0:
            yield i
            if i*i != n:
                large_divisors.append(n / i)
    for divisor in reversed(large_divisors):
        yield divisor
