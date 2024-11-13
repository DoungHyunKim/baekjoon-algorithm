t = int(input())

for i in range(t):
    matrix = int(input())
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    # 2차원 배열 0으로 초기화
    snale = [[0] * matrix for _ in range(matrix)]
    
    # 초기 좌표 초기화
    x = y = 0
    move = 0

    for j in range(matrix**2):
        snale[x][y] = (j + 1)
        nx = x + dx[move]
        ny = y + dy[move]

        if 0 <= nx < matrix and 0 <= ny < matrix and snale[nx][ny] == 0:
            x, y = nx, ny
        else:
            move = (move + 1) % 4
            x += dx[move]
            y += dy[move]

    print(f"#{i + 1}")
    for k in snale:
        print(*k) 