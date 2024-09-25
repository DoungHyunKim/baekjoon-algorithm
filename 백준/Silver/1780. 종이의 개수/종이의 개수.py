import sys
input = lambda: sys.stdin.readline().rstrip()

K = int(input())
paper = [list(map(int, input().split())) for _ in range(K)]

result = []

def div(x, y, K):
    number = paper[x][y]

    for i in range(x, x + K):
        for j in range(y, y + K):
            if number != paper[i][j]:  # 종이 값이 다르면 9등분
                for dx in range(3):
                    for dy in range(3):
                        div(x + dx * K // 3, y + dy * K // 3, K // 3)
                return
    if number == 0:
        result.append(0)
    elif number == 1:
        result.append(1)
    else:
        result.append(-1)

div(0, 0, K)

print(result.count(-1))
print(result.count(0))
print(result.count(1))
