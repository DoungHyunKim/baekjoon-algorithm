N = int(input())
num_list = map(int, input().split())
compare_num = int(input())
count = 0

for num in num_list:
    if num == compare_num:
        count += 1

print(count)