import sys
input = lambda: sys.stdin.readline().rstrip()

def tile(num):
    dp = [0] * (num + 1)
    dp[1] = 1
    if num > 1:
        dp[2] = 2
    
    for i in range(3,num + 1):
        dp[i] = (dp[i-1] + dp[i-2]) % 15746
    
    return dp[num]

def main():
    N = int(input())
    print(tile(N))

if __name__ == "__main__":
    main()