import sys
input =lambda: sys.stdin.readline().rstrip()

size = map(int, input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

result = a + b
print(*sorted(result))