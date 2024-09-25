import sys
sys.setrecursionlimit(10**7)
input = lambda: sys.stdin.readline().strip()

N = int(input())

E = int(input())

graph = [[] for _ in range(N+1)]
visited = [False] * (N + 1)

for _ in range(E):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

def dfs(v):
    visited[v] = True
    
    for i in graph[v]:
        if not visited[i]:
            visited[i] = True
            dfs(i)
dfs(1)
print(visited.count(True) - 1)