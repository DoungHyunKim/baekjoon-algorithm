import sys
from collections import Counter
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
arr1 = list(map(int, input().split()))
M = int(input())
arr2 = list(map(int, input().split()))

arr1_counter = Counter(arr1)

result = [arr1_counter[i] for i in arr2]

print(*result)