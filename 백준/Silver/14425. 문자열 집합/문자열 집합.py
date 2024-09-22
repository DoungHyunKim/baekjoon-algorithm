import sys
input = lambda: sys.stdin.readline().rstrip()

N, S = map(int, input().split())

str_arr = list()

for _ in range(N):
    str_arr.append(input())

str_arr2 = []
for _ in range(S):
    str_arr2.append(input())

count = 0

for i in str_arr2:
    if i in str_arr:
        count += 1

print(count)