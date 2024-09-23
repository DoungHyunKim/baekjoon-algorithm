import sys
input = lambda: sys.stdin.readline().rstrip()

N, K = map(int, input().split())  # 동전 종류 N개, 목표 금액 K

coin_type = [int(input()) for _ in range(N)]  # N개의 동전 종류 입력받기
coin_type = sorted(coin_type, reverse=True)  # 큰 동전부터 사용하기 위해 내림차순 정렬

count = 0  # 동전 개수 카운트

for coin in coin_type:  # 가장 큰 동전부터 차례로 확인
    if K == 0:
        break  # K가 0이면 더 이상 계산할 필요 없음
    count += K // coin  # 해당 동전으로 만들 수 있는 개수만큼 카운트
    K %= coin  # 나머지 금액을 계산

print(count)  # 최종 동전 개수 출력
