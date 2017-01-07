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

