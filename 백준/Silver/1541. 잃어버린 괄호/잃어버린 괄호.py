str = input().split('-')
num_list = []

for i in str:
    plus = i.split('+')
    sum = 0
    for j in plus:
        sum += int(j)
    num_list.append(sum)

first_num = num_list[0]

for i in range(1,len(num_list)):
    first_num -= num_list[i]

print(first_num)