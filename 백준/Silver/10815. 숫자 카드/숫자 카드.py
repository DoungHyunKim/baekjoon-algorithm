import sys
input = lambda: sys.stdin.readline().strip()

# 첫 번째 배열 입력 받기
N = int(input())
arr1 = set(map(int, input().split()))  # 1차원 리스트로 입력받음

# 두 번째 배열 입력 받기
M = int(input())
arr2 = list(map(int, input().split()))  # 1차원 리스트로 입력받음

# 결과를 저장할 리스트
result = []

# arr2의 각 원소가 arr1에 있는지 확인
for i in arr2:
    if i in arr1:
        result.append(1)
    else:
        result.append(0)

# 결과 출력
print(*result)
