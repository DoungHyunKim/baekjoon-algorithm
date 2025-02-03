# 대문자 A는 65 소문자 a 는 97 z는 122
# 65~122 사이의 수는 알파벳 대소문자이다.
# for문을 돌면서 문자를 담아두고 만약 65 -122 사이의 숫자가 나오면 리스트를 정수로 바꾸고 더하자
# a = ord('6')
# print(a)
import sys
input = lambda: sys.stdin.readline().rstrip()

# 단어의 길이
how_many_nums = int(input())

num_list = []
# print(int(''.join(num_list)) + 1)

# 단어 입력
sentence = input()
#print("sentence : ",sentence)

# 총합
sum = 0

for find_num in sentence:
    #print("find_num : ", find_num)

    if 65<= ord(find_num) <= 122:
        #print("num_list : ",num_list)
        if(num_list):
            sum += int(''.join(num_list))
            #print("sum : ", sum)
        num_list.clear()
    # else로 한 이유 단어는 알파벳 대/소문자와 숫자로 이루어져 있음. 특수 문자는 없다.
    else:
        num_list.append(find_num)
        #print("num_list2: ", num_list)

if num_list:
    sum += int(''.join(num_list))
print(sum)
