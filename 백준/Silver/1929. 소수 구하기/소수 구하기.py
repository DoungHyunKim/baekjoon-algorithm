import sys, math
input = lambda: sys.stdin.readline().rstrip()

M, N = map(int, input().split())

def isPrime(number):
    if number < 2:
        return False
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True


for i in range(M,N+1):
    if isPrime(i):
        print(i)
