N = int(input())
count = 0

while N >= 0:
    if N % 5 == 0:  # 5로 나누어 떨어질 때
        count += N // 5
        print(count)
        break
    N -= 3  # 5로 나눠지지 않으면 3을 빼고 카운트 증가
    count += 1
else:
    print(-1)  # 정확히 0이 되지 않으면 -1 출력
