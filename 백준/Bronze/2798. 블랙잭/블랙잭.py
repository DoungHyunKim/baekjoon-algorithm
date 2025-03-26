from itertools import combinations
import sys
input = lambda : sys.stdin.readline().rstrip()

N, M = map(int, input().split())
numbers = map(int, input().split())

num_list = list(combinations(numbers, 3))

max_num = 0
for  combination in num_list:
    if sum(combination) <= M:
        max_num = max(max_num, sum(combination))

print(max_num)