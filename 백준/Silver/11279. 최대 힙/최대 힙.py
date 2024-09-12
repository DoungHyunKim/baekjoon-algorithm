import sys, heapq

input = lambda: sys.stdin.readline().rstrip()

# 입력 받기
N = int(input())

# 최대 힙을 위한 리스트
max_heap = []

for _ in range(N):
    num = int(input())

    if num == 0:
        if max_heap:
            # 최대 힙에서 최댓값 꺼내기
            print(-heapq.heappop(max_heap))
        else:
            print(0)  # 힙이 비어 있을 때
    else:
        # 최대 힙에 값 추가 (음수로 넣어서 최대 힙 구현)
        heapq.heappush(max_heap, -num)