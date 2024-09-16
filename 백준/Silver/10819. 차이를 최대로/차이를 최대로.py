import sys
from itertools import permutations

input = lambda: sys.stdin.readline().rstrip()

N = int(input())
num_list = []


num_list = map(int, input().split())

per_list = list(permutations(num_list))
real_sum = 0

for per in per_list:
    per_sum = 0
    for j in range(len(per) - 1):
        per_sum += abs(per[j] - per[j+1])
    if per_sum > real_sum:
        real_sum = per_sum

print(real_sum)