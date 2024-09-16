import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
num_list = []

for _ in range(n):
    num = int(input())
    
    if num == 0:
        if num_list:  # 리스트가 비어있지 않을 때만 pop
            num_list.pop()  # 가장 최근에 추가된 요소 제거
    else:
        num_list.append(num)

# 남은 숫자들의 합을 출력
print(sum(num_list))
