from collections import deque

t = int(input())

for _ in range(t):
    # 가로, 세로, 배추가 심어져 있는 위치의 개수 
    m, n, k = map(int, input().split())
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    # 배추 밭 초기화
    area = [[0] * m for _ in range(n)]

    # 배추가 심어져 있는 땅 구하기  
    for _ in range(k):
        x, y = map(int, input().split())
        area[y][x] = 1  # 문제 정의에 따라 x는 가로, y는 세로 좌표

    # 전체 필요한 지렁이 초기화
    total_warm = 0

    # 방문 확인 배열
    visited = [[False] * m for _ in range(n)]

    # BFS 탐색 함수
    def bfs(start_x, start_y):
        queue = deque([(start_x, start_y)])
        visited[start_y][start_x] = True

        while queue:
            x, y = queue.popleft()

            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]

                if 0 <= nx < m and 0 <= ny < n and not visited[ny][nx] and area[ny][nx] == 1:
                    visited[ny][nx] = True
                    queue.append((nx, ny))

    # 배추 밭 전체 탐색
    for y in range(n):
        for x in range(m):
            if area[y][x] == 1 and not visited[y][x]:
                bfs(x, y)
                total_warm += 1
    
    print(total_warm)
