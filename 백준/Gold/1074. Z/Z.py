n, r, c = map(int, input().split())
count = 0

def zcount(n, x, y):
    global count
    if x == r and y == c:
        print(count)
        exit(0)  

    if n == 1:
        count += 1
        return 
    
    # 현재 영역이 목표 좌표를 포함하지 않는 경우
    if not (x <= r < x + n and y <= c < y + n):
        count += n * n  # result -> count로 수정
        return

    # 1사분면
    zcount(n // 2, x, y)
    # 2사분면
    zcount(n // 2, x, y + n // 2)
    # 3사분면
    zcount(n // 2, x + n // 2, y)
    # 4사분면
    zcount(n // 2, x + n // 2, y + n // 2)

zcount(2**n, 0, 0)
