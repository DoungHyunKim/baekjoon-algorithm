import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())

# 입력 리스트
num_list = list(map(int, input().split()))

# 리스트를 정렬
num_list.sort()

# 투 포인터 설정
left = 0
right = N - 1

# 0에 가장 가까운 합과 그때의 두 숫자를 저장
closest_sum = float('inf')
closest_pair = (0, 0)

# 투 포인터 알고리즘
while left < right:
    current_sum = num_list[left] + num_list[right]
    
    # 현재 합이 더 0에 가깝다면 갱신
    if abs(current_sum) < abs(closest_sum):
        closest_sum = current_sum
        closest_pair = (num_list[left], num_list[right])
    
    # 합이 0보다 크면 오른쪽 포인터를 왼쪽으로 이동
    if current_sum > 0:
        right -= 1
    # 합이 0보다 작으면 왼쪽 포인터를 오른쪽으로 이동
    elif current_sum < 0:
        left += 1
    else:
        # 합이 정확히 0이면 더 찾을 필요 없음
        break

# 결과 출력
print(closest_pair[0], closest_pair[1])
