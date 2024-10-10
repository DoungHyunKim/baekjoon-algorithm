from collections import Counter

def is_same(a, b):
    if Counter(a) == Counter(b):
        return "Possible"
    else:
        return "Impossible"

N = int(input())

for _ in range(N):
    a, b = input().split()
    print(is_same(a, b))
