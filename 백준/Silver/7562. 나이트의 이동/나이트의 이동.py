from collections import  deque
import sys
input = lambda: sys.stdin.readline().rstrip()

# 나이트는 한자리에서 최대 8곳을 방문할 수 있다. 
dx = [2, 1, -2, -1, 2, 1, -2, -1]
dy = [1, 2, 1, 2, -1, -2, -1, -2]

def bfs(init_x, init_y, destianation_x, destianation_y,  chess_board):
    queue = deque([(init_x, init_y)])

    # 실수 2: 시작점에서  끝점이 같을 때, 돌고 돌아 다시함. 
    # init_x, init_y 초기화해야됨. 1로 초기화 하기엔 출력값이 0이 나오기 쉽지 않음. 
    if init_x == destianation_x and init_y == destiantion_y:
        return 0
    
    while queue:
        # 실수 1. queue.popleft()를 해야되는 데 pop() 을 해서 원하는 결과값이  나오지 않음. 
        x, y = queue.popleft()
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and chess_board[nx][ny] == 0:
                chess_board[nx][ny] = chess_board[x][y] + 1
                queue.append((nx, ny))

    return chess_board[destianation_x][destianation_y]

# test case
t = int(input())

for i in range(t):
    # n x n 체스판
    n = int(input())

    # 채스판 초기화
    chess_board = [[0] * n for _ in range(n)]

    # 방문 여부 
    # visited = [[False] * n for _ in range(n)]
    # 방문 여부는 따로 처리할 필요가 없어보임.

    # 현재 나이트의 위치
    init_x, init_y = map(int, input().split())
    
    # 나이트의 최종 목적지 좌표
    destiantion_x, destiantion_y = map(int, input().split())

    print(bfs(init_x, init_y,  destiantion_x, destiantion_y, chess_board))