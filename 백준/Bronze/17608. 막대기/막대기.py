def count_visual_stick(heights):
    count = 0
    max_height = 0
    for height in reversed(heights):
        if height > max_height:
            count += 1
            max_height = height
    return count
import sys

input = lambda: sys.stdin.readline().rstrip()

N = int(input())
heights = []

for i in range(N):
    heights.append(int(input()))

print(count_visual_stick(heights))