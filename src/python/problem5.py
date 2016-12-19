'''
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
Ans: 232792560
'''

def divisibleList2(number, factors):
    return all(map(lambda x: number%x == 0, factors))

def solution():
    numbers = range(11, 21)
    result = 2520
    while True:
        if divisibleList2(result, numbers):
            return result
        result += 20

if __name__ == "__main__":
    print solution()
