import sys
sys.setrecursionlimit(10**7)
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
visited = [False] * (N + 1)
graph = [[] for _ in range(N+1)]

for i in range(N-1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
parent = [[] for _ in range(N+1)]

def dfs(v):
    visited[v] = True
    
    for i in graph[v]:
        if not visited[i]:
            parent[i] = v
            visited[i] = True
            dfs(i)
dfs(1)

for i in range(2,N+1):
    print(parent[i])