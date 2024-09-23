import sys

input = lambda: sys.stdin.readline().rstrip()

N = int(input())

times = list(map(int, input().split()))
times = sorted(times)

per_time = []

for i in range(len(times)+1):
    per_time.append(times[:i])

# print(per_time)
time_sum= 0

for i in per_time:
    for j in i:
        time_sum += j
        # print(time_sum)

print(time_sum)