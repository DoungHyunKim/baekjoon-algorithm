from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y, grid, visited, n, color_blind):
    queue = deque([(x, y)])
    visited[x][y] = True
    current_color = grid[x][y]

    while queue:
        cx, cy = queue.popleft()
        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            if 0 <= nx < n  and 0 <= ny < n and not visited[nx][ny]:
                if color_blind:
                    if current_color in "RG" and grid[nx][ny] in "RG":
                        visited[nx][ny] = True
                        queue.append((nx, ny))
                    elif grid[nx][ny] == current_color:
                        visited[nx][ny] = True
                        queue.append((nx, ny))
                else:
                    if grid[nx][ny] == current_color:
                        visited[nx][ny] = True
                        queue.append((nx, ny))

n = int(input())
grid = [input().strip() for _ in range(n)]

visited_normal = [[False] * n for _ in range(n)]
normal_count = 0

visited_blind = [[False] * n for _ in range(n)]
blind_count = 0

for i in range(n):
    for j in range(n):
        if not visited_blind[i][j]:
            bfs(i, j, grid, visited_blind, n, True)
            blind_count += 1
        if not visited_normal[i][j]:
            bfs(i, j, grid, visited_normal, n , False)
            normal_count += 1

print(normal_count, blind_count)