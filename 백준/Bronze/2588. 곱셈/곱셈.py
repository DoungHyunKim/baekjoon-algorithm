import sys

input = lambda: sys.stdin.readline().rstrip()

n = 3
num1 = input()
num2 = input()
result = 0

for i in range(n):
    nth = 10**i
    multify = int(num1) * int(num2[n-1-i]) 
    print(multify)
    result += multify * nth

print(result)
