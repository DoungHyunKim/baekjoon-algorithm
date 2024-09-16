import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
tops = list(map(int, input().split()))

stack = []
top_connect = [0] * N

for i in range(N):
    # Check for the first taller tower to the left
    while stack and tops[stack[-1]] <= tops[i]:  # Changed < to <= to match the first code logic
        stack.pop()
    if stack:
        top_connect[i] = stack[-1] + 1  # Record the index (1-based)
    stack.append(i)

print(*top_connect)