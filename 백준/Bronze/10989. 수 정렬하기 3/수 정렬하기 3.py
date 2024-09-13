import sys

input = lambda: sys.stdin.readline().rstrip()

N = int(input())  # 입력받을 숫자의 개수
max_value = 10000  # 숫자의 범위가 0부터 10000까지라고 가정

num_list = [0] * (max_value + 1)  # 0부터 max_value까지의 숫자의 빈도를 저장할 리스트

# 각 숫자의 빈도를 카운트
for _ in range(N):
    num_list[int(input())] += 1

# 숫자를 오름차순으로 출력
for i in range(len(num_list)):
    if num_list[i] != 0:  # 숫자가 존재할 경우
        for _ in range(num_list[i]):
            print(i)
