import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
common_log = {}

for _ in range(N):
    u,v = input().split()
    common_log[u] = v

enter_people = [key for key, value in common_log.items() if value == 'enter']

enter_people = sorted(enter_people, reverse=True)
for i in enter_people:
    print(i)

