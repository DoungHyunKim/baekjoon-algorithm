import sys

input = lambda: sys.stdin.readline().strip()

N = int(input())

for i in range(N):
    result = 0
    cnt = 0
    ox = input()
    for j in ox:
        if j == 'O':
            cnt += 1
        else:
            cnt = 0
        result += cnt
    print(result)