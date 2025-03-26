import sys

input = lambda: sys.stdin.readline().rstrip()

N = int(input())

# N의 가장 작은 생성자를 찾기 위한 브루트포스
for i in range(1, N + 1):
    # 각 숫자의 분해합을 계산
    sums = i + sum(int(digit) for digit in str(i))

    # 생성자를 찾으면 출력하고 종료
    if sums == N:
        print(i)
        exit()

# 생성자가 없으면 0 출력
print(0)