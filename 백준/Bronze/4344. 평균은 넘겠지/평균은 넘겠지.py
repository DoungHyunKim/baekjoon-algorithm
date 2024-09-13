import sys
input = lambda: sys.stdin.readline().rstrip()

C = int(input())


for _ in range(C):
    cnt = 0
    result = 0
    score = list(map(int,input().split()))
    average = sum(score[1:]) / len(score[1:])
    for i in range(score[0]):
        if score[i+1] > average:
            cnt += 1
    result = round((cnt /score[0]) * 100, 3)    
    print(f'{result}%')
    score.clear()