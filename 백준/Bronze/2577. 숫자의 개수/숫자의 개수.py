A = int(input())
B = int(input())
C = int(input())

multify = str(A * B * C)

list_numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

for i in list_numbers:
    index = multify.count(i)
    if index != -1:  # 문자가 존재하는 경우
        print(index)
    else:
        print(0)