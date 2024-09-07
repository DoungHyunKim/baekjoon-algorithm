# 소수 찾기 
n = int(input())

nums_list = map(int, input().split()) 
results = 0

for i in nums_list:    # nums_list = [1, 3, 5, 7]
    cnt = 0

    for j in range(1,i):
        if i %  j == 0:
            cnt += 1
        
    if cnt == 1:
        results += 1

print(results)
