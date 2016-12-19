'''
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 * 99.

Find the largest palindrome made from the product of two 3-digit numbers.
'''

def solution():
    num1, num2 = 999, 999
    result = []
    while num1 >= 100:
        num2 = 999
        while num2 >= 100:
            number = str(num1*num2)
            if number == number[::-1]:
                result.append(num1*num2)
            num2 -= 1
        num1 -= 1
    return max(result)

if __name__ == "__main__":
    print solution()
