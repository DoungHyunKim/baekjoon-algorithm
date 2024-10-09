import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
n_list = sorted(map(int, input().split()))
compare_num = int(input())
count = 0

left, right = 0, N-1

while left < right:
    combi_sum = n_list[left] + n_list[right]
    
    if combi_sum == compare_num:
        count += 1
        left += 1
        right -= 1
    elif combi_sum < compare_num:
        left += 1
    elif combi_sum > compare_num:
        right -= 1
    else:
        print("그런 조합 없다~")

print(count)