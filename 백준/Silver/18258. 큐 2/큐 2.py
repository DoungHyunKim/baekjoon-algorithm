import sys
from collections import deque

N = int(sys.stdin.readline().rstrip())  # 명령어의 수 N 

queue = deque([])

for _ in range(N):
    command = sys.stdin.readline().rstrip().split()
    
    if command[0] == 'push':  # push x
        queue.append(int(command[1]))  # 정수로 변환하여 추가
    elif command[0] == 'pop':  # queue의 0번째 인덱스 삭제
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.popleft())
    elif command[0] == 'size':  # 큐에 들어있는 정수의 개수
        print(len(queue))
    elif command[0] == 'empty':  # 큐가 비어 있는지 확인
        if len(queue) == 0:
            print(1)  # 큐가 비어 있으면 1
        else:
            print(0)  # 큐가 비어 있지 않으면 0
    elif command[0] == 'front':  # 큐의 첫 번째 요소 출력
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
    elif command[0] == 'back':  # 큐의 마지막 요소 출력
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])
