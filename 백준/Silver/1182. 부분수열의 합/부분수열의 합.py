import sys
from itertools import combinations

input = lambda: sys.stdin.readline().rstrip()

combination = []

N, S  = map(int, input().split())

number = map(int, input().split())
number = list(number)
# print('number',number)

# for문으로 조합의 개수를 늘려서 1이 되는 경우를 찾자.

for i in range(1,N+1):
    combination.append(list(combinations(number, i)))

# print('combination : ',combination)
# print('combination 길이 :',len(combination))

count = 0
if (len(number) == 1 and number[0] == S):
    count = 1
else:
    for i in range(len(combination)):
        for j in range(len(combination[i])):
            if (sum(combination[i][j]) == S):
                count += 1
                # print(combination[i][j])


# print('count : ',count)
print(count)