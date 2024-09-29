import sys
input = lambda: sys.stdin.readline().rstrip()

def coin_count(coin_type, money):
    dp = [0] * (money + 1)
    dp[0] = 1

    for coin in coin_type:
        for amount in range(coin, money + 1):
            dp[amount] += dp[amount - coin]
    return dp[money]

test_case = int(input())

for _ in range(test_case):
    N = int(input())
    coin_type = map(int, input().split())
    money = int(input())

    print(coin_count(coin_type, money))