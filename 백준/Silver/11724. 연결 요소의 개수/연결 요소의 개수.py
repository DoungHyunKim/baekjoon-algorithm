import sys
sys.setrecursionlimit(10**7)
input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())

graph = [[] for i in range(N+1)]

visited = [False] * (N+1)

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

def dfs(u):
    visited[u] = True

    for i in graph[u]:
        if not visited[i]:
            visited[i] = True
            dfs(i)
count = 0 

for i in range(1, N + 1):
    if not visited[i]:
        dfs(i)
        count += 1

print(count)
