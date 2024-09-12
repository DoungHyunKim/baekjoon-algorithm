import sys
input = lambda: sys.stdin.readline().rstrip()

N , X = map(int,input().split())

A = list(map(int, input().split()))

resuit = []
for i in A:
    if (X > i):
        print(i, end= ' ')