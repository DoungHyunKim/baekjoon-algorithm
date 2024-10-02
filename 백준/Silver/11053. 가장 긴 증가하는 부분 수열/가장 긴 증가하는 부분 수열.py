import sys, bisect
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
A = list(map(int, input().split()))
lis = []

for num in A:
    pos = bisect.bisect_left(lis, num)

    if pos < len(lis):
        lis[pos] = num
    else:
        lis.append(num)

print(len(lis))