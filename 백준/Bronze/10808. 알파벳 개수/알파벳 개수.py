word = input()
dp = [0] * 26 # 알파벳의 개수 

for alpha in word:
    location = ord(alpha) % ord('a')
    dp[location] += 1

print(*dp) 