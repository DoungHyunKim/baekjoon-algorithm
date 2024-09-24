import sys
input = lambda: sys.stdin.readline().rstrip()

V, E = map(int, input().split())

# 크루스칼 알고리즘
edges = []
for _ in range(E):
    A, B, C = map(int, input().split())
    edges.append((A, B, C))
edges.sort(key=lambda x: x[2])  # 비용으로 정렬

# 유니온-파인드
parent = [i for i in range(V + 1)]

def get_parent(x):
    stack = []
    while parent[x] != x:
        stack.append(x)
        x = parent[x]
    root = x
    # 경로 압축
    while stack:
        parent[stack.pop()] = root
    return root

def union_parent(a, b):
    a = get_parent(a)
    b = get_parent(b)

    if a != b:
        if a < b:  # 작은 쪽이 부모가 된다
            parent[b] = a
        else:
            parent[a] = b

def same_parent(a, b):
    return get_parent(a) == get_parent(b)

answer = 0
for a, b, cost in edges:
    if not same_parent(a, b):
        union_parent(a, b)
        answer += cost

print(answer)
