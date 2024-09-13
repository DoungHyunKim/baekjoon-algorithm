n = int(input())

cnt = 0
original = n

def back(new_num):
    global cnt
    cnt += 1
    
    num1 = new_num % 10
    num2 = new_num // 10

    sums = num1 + num2
    new_num = (num1 * 10) + (sums % 10)

    if new_num == original:
        print(cnt)
        return
    else:
        back(new_num)

back(n)
