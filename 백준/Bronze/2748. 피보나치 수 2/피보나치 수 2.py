def fibo(N):
    if N == 0:
        return 0
    elif N == 1:
        return 1
    
    if dp[N] != 0:
        return dp[N]
    
    dp[N] = fibo(N-1) + fibo(N-2)

    return dp[N]

N = int(input())
dp = [0] * (N+1)
print(fibo(N))
