import sys, math
input = lambda: sys.stdin.readline().rstrip()

N = int(input())  # 입력 개수 N

prime = [int(input()) for _ in range(N)]  # N개의 입력 숫자 리스트

def isPrime(number):
    if number < 2:
        return False
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True

def makePrime(number):
    if number <= 1:  # 0 또는 1은 2로 처리
        return 2
    
    while not isPrime(number):  # 소수가 나올 때까지 반복
        number += 1
    return number

for i in prime:
    if isPrime(i):
        print(i)
    else:
        print(makePrime(i))  # 소수가 아닌 경우 가장 가까운 소수를 출력
