from collections import deque

# 가로 세로 크기
n, m = map(int, input().split())

# 도화지
canvas = [list(map(int, input().split())) for _ in range(n)]

# 방문 여부
visited = [[False] * m for _ in range(n)]

# 그림의 개수
num_of_pictures = 0

# 가장 넓은 그림
max_size = 0

def bfs(x, y):
    queue = deque([(x, y)])
    visited[x][y] = True

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    size = 1 # 현재 도화지의 크기

    while queue:
        cx, cy = queue.popleft()
        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            if 0 <= nx <n and 0 <= ny < m and not visited[nx][ny] and canvas[nx][ny] == 1:
                visited[nx][ny] = True
                queue.append((nx, ny))
                size += 1
    return size

for i in range(n):
    for j in range(m):
        if canvas[i][j] == 1 and not visited[i][j]:
            num_of_pictures += 1
            max_size = max(max_size, bfs(i, j))

print(num_of_pictures)
print(max_size)