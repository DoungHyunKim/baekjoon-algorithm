# 공유기 사이의 최소 거리를 최대화? 

def install_routers(houses, C):
    # 집 좌표를 정렬
    houses.sort()

    # 이분 탐색을 위한 초기 값 설정
    left = 1  # 가능한 최소 거리
    right = houses[-1] - houses[0]  # 가능한 최대 거리
    answer = 0

    # 이분 탐색
    while left <= right:
        mid = (left + right) // 2  # 공유기 사이의 중간 거리

        # 첫 번째 집에 공유기 설치
        current = houses[0]
        count = 1

        # 다음 공유기 설치
        for i in range(1, len(houses)):
            if houses[i] >= current + mid:
                current = houses[i]
                count += 1

        # 설치된 공유기 개수가 목표치 이상이면, 거리를 늘려본다.
        if count >= C:
            answer = mid
            left = mid + 1
        # 설치된 공유기 개수가 부족하면, 거리를 줄인다.
        else:
            right = mid - 1

    return answer

import sys
input = lambda: sys.stdin.readline().rstrip()

N, C = map(int,input().split())

houses = []

for _ in range(N):
    houses.append(int(input()))

print(install_routers(houses,C))