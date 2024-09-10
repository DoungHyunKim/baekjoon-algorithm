arr1_N = int(input())
arr1 = set(map(int, input().split()))  # set으로 변환하여 탐색 시간 O(1)로 줄임
arr2_N = int(input())
arr2 = list(map(int, input().split()))

# check_arr 초기화
check_arr = [0] * len(arr2)

# arr2의 각 원소가 arr1에 있는지 확인
for i in range(len(arr2)):
    if arr2[i] in arr1:  # O(1)로 탐색 가능
        check_arr[i] = 1
    else:
        check_arr[i] = 0

# 결과 출력
for num in check_arr:
    print(num)