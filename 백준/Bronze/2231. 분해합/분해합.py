N = int(input())
start = max(1, N - len(str(N)) * 9)
answer = 0

for i in range(start, N + 1):
    result = i
    for digit in str(i):
        result += int(digit)
    if result == N:
        answer = i
        break

print(answer)
