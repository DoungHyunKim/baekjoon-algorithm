import sys

N = int(input())
num_list = []

# N번 입력 받기
for _ in range(N):
    num_list.append(int(sys.stdin.readline().rstrip()))

# 중복된 수 제거 및 정렬
num_list = sorted(set(num_list))

# 오름차순 정렬된 리스트 출력
for num in num_list:
    print(num)
