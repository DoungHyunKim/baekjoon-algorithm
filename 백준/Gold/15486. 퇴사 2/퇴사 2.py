import sys
input = lambda: sys.stdin.readline().rstrip()

def max_advice_fee(advice):
    M = len(advice)
    dp = [0] * (M + 1)

    for i in range(1, M + 1):
        # 현재 날짜에서 상담이 끝나는 날짜를 계산
        if i + advice[i-1][0] <= M + 1:
            # 상담을 하는 경우
            dp[i + advice[i-1][0] - 1] = max(dp[i + advice[i-1][0] - 1], dp[i-1] + advice[i-1][1])
        
        # 상담을 하지 않는 경우
        dp[i] = max(dp[i], dp[i-1])
    
    return dp[M]

def main():
    N = int(input())
    advice = [tuple(map(int, input().split())) for _ in range(N)]
    
    print(max_advice_fee(advice))

if __name__ == "__main__":
    main()
