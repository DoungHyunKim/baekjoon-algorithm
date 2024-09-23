def factorial(number):
    if number <=1:
        return 1
    return number * factorial(number-1)

import sys
input = lambda: sys.stdin.readline().rstrip()
print(factorial(int(input())))