'''
2520 is the smallest number that can be divided by
each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly
divisible by all of the numbers from 1 to 20?
Ans: 232792560
'''

import util


def solution():
    '''
    Returns:
        Smallest +ve number that is evenly divisible by all numbers 
        from 1 to 20
    '''
    numbers = range(11, 21)
    result = 2520
    while True:
        if util.divisibleByWholeList(result, numbers):
            return result
        result += 20


if __name__ == "__main__":
    print solution()
