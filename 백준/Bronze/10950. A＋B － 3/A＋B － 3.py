import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())

for i in range(N):
    a,b = map(int, input().split())
    sums = a + b
    print(sums)