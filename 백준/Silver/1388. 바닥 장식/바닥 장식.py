n, m = map(int, input().split())
array = []
count = 0

visited = [[False] * m for _ in range(n)]

def dfs(x, y):
    visited[x][y] = True
    if array[x][y] == '|' :
        if x+1<n and array[x+1][y] == '|' and visited[x+1][y]==False:
            dfs(x+1, y)
        else:
            return
    if array[x][y] == '-' :
        if y+1<m and array[x][y+1] == '-' and visited[x][y+1]==False:
            dfs(x, y+1)
        else:
            return
        

for _ in range(n):
    array.append(list(input()))
        
for i in range(n):
    for j in range(m):
        if not visited[i][j]:
            dfs(i, j)
            count+=1
print(count)