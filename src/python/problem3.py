'''
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''

import util

def solution():
    number = 600851475143
    if number%2 == 0:
        factors = [2]
    else:
        factors = [3]
    prime = 3
    while number > 1:
        if number%prime == 0 and not divisibleByAnyInList(prime, factors):
            factors.append(prime)
            number = number / prime
        prime += 2
    return max(factors)

if __name__ == "__main__":
    print solution()
