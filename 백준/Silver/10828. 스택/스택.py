import sys

N = int(sys.stdin.readline().rstrip())
commnad_list = []
stack = []

for i in range(N):
    commnad_list.append(list(sys.stdin.readline().rstrip().split()))
    if len(commnad_list[-1]) == 2:
        stack.append(int(commnad_list[-1][1]))
    elif commnad_list[-1][0] == 'top':
        if (len(stack)):
            print(stack[-1])
        else:
            print(-1)
    elif commnad_list[-1][0] == 'size':
        print(len(stack))
    elif commnad_list[-1][0] == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    else:
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())