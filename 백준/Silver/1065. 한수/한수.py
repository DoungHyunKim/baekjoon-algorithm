N =  int(input())
hansu = 0

for i in range(1,N+1):
    if i < 100:
        hansu += 1
    else:
        i = str(i)
        if (int(i[0]) - int(i[1]) == int(i[1]) - int(i[2])):
            hansu += 1

print(hansu)