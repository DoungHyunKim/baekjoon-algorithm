from itertools import combinations

N = 9
num_list = []

# 9개의 숫자를 입력받아 리스트에 저장
for i in range(N):
    num_list.append(int(input()))

# 9명 중에서 7명을 고르는 모든 조합을 구함
seven_combinations = list(combinations(num_list, 7))

# 각 조합의 합이 100인 경우를 찾음
for seven in seven_combinations:
    if sum(seven) == 100:
        # 합이 100인 조합을 오름차순으로 정렬하고 출력
        sorted_seven = sorted(seven)
        for num in sorted_seven:
            print(num)
        exit()
