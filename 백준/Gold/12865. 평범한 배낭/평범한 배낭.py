import sys
input = lambda: sys.stdin.readline().rstrip()

N, K = map(int, input().split())

items = [list(map(int, input().split())) for _ in range(N)]

def knapsack(items, K):
    M = len(items)
    dp = [[0] * (K + 1) for _ in range(M + 1)]

    for i in range(1, M + 1):
        for j in range(1, K + 1):  
            if j >= items[i - 1][0]:  
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - items[i - 1][0]] + items[i - 1][1])  # 인덱스 수정
            else:
                dp[i][j] = dp[i - 1][j]
                
    return dp[M][K] 

print(knapsack(items, K))
