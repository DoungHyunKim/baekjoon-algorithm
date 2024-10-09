result = 1
for _ in range(3):
    N = int(input())
    result *= N
dp = [0] * 10

for num in str(result):
    location = int(num) % 10
    dp[location] += 1

for i in dp:
    print(i)