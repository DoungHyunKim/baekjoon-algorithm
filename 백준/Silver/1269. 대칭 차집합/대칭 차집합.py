import sys
input = lambda: sys.stdin.readline().rstrip()

a_size, b_size = map(int, input().split())
a = set(map(int, input().split()))
b = set(map(int, input().split()))

print((len(a) + len(b)) - (len(a & b) * 2) )