N = int(input())
km = list(map(int, input().split()))
cost = list(map(int, input().split()))

min_price = cost[0] 
total = 0

for i in range(len(km)):
    if min_price > cost[i]:
        min_price = cost[i]
    total += (min_price * km[i])

print(total)