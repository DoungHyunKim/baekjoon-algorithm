N = int(input())  # N = 1
dp = [0] * (N + 1)  # dp = [0, 0]
dp[1] = 1
if N > 1:  # N이 1보다 클 때만 실행
    dp[2] = 2  # 이 코드는 실행되지 않음

for i in range(3, N + 1):
    dp[i] = (dp[i-1] + dp[i-2]) % 15746

print(dp[N])
