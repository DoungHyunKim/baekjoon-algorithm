import sys
input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())
trees = list(map(int, input().split()))  
start, end = 0, max(trees)

while start <= end:
    cutting_tree = (start + end) // 2
    tree_sum = 0

    for tree in trees:
        if tree > cutting_tree:
            tree_sum += tree - cutting_tree
    
    if tree_sum >= M:
        start = cutting_tree + 1  # 더 높은 절단 높이를 찾아봄
    else:
        end = cutting_tree - 1  # 더 낮은 절단 높이를 찾아봄

print(end)