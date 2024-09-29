def lcs(X, Y):
    M = len(X)
    N = len(Y)

    dp = [[0]*(N+1) for _ in range(M+1)]

    for i in range(1, M+1):
        for j in range(1, N+1):
            if X[i-1] == Y[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
    return dp[M][N]                                                                                       

X = input()
Y = input()

print(lcs(X,Y))