'''
Handy functions to use in solving other problems
'''

def divisibleByWholeList(number, factors):
    return all(map(lambda x: number%x == 0, factors))

def divisibleByAnyInList(number, factors):
    return any(map(lambda x: number%x == 0, factors))
