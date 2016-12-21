'''
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a^2 + b^2 = c^2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
'''


def solution():
    num1 = 1
    while num1 <= 998:
        num2 = 1
        while num2 < 1000 - num1:
            num3 = 1000 - num1 - num2
            if (num1 ** 2 + num2 ** 2 == num3 ** 2 or
                    num1 ** 2 + num3 ** 2 == num1 ** 2 or
                    num2 ** 2 + num3 ** 2 == num1 ** 2):
                return num1 * num2 * num3
            num2 += 1
        num1 += 1


if __name__ == "__main__":
    print solution()
