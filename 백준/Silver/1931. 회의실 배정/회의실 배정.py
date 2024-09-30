def find_max(meettings):
    meettings = sorted(meettings, key=lambda x: (x[1],x[0]))
    end_time = 0
    count = 0

    for start, end in meettings:
        if start >=end_time:
            count += 1
            end_time = end
    
    return count

import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
meettings = [list(map(int, input().split())) for _ in range(N)]

print(find_max(meettings))