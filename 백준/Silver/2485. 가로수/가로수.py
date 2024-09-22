import sys, math
input = lambda: sys.stdin.readline().rstrip()

N = int(input())

trees = [int(input()) for _ in range(N)]

distances = [trees[i] - trees[i-1] for i in range(1,N)]

gcd = distances[0]

for d in distances[1:]:
    gcd = math.gcd(gcd, d)

new_trees = (trees[-1] - trees[0]) // gcd - (N-1)

print(new_trees)