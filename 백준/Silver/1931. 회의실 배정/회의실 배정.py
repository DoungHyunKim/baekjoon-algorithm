import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
meetings = [list(map(int, input().split())) for _ in range(N)]

sorted_meetings = sorted(meetings, key=lambda x: (x[1], x[0]))

# 회의 선택 카운트 및 마지막으로 선택된 회의의 종료 시간
count = 0
last_end_time = 0

for meeting in sorted_meetings:
    start, end = meeting
    if start >= last_end_time:
        count += 1
        last_end_time = end

print(count)