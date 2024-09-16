import sys, heapq
input = lambda: sys.stdin.readline().rstrip()

N = int(input())

max_heap = []
min_heap = []

for i in range(N):
    num = int(input())
    heapq.heappush(max_heap, -num)

    if max_heap:
        heapq.heappush(min_heap, -heapq.heappop(max_heap))
    
    if len(max_heap) < len(min_heap):
        heapq.heappush(max_heap, -heapq.heappop(min_heap))
    if len(max_heap) > len(min_heap):
        print(-max_heap[0])
    else:
        print(-max_heap[0])
        