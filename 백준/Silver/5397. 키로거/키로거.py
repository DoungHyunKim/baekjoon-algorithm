''''
< 를 만나면 오른쪽 스택에
> 를 만나면 왼쪽 스택에 
- 를 만나면 왼쪽 스택을 pop
만약 오른쪽 스택이 남아 있다면 붙일 때 오른쪽으로 한칸 이동 
'''
import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())

for _ in range(N):
    password = input()
    leftStack = []
    rightStack = []
    cur = 0
    
    for str in password:
        if str == "<":
            if leftStack:
                rightStack.append(leftStack.pop())
                cur -= 1
        elif str == ">":
            if rightStack:
                leftStack.append(rightStack.pop())
                cur += 1
        elif str == "-":
            if leftStack:
                leftStack.pop()
        else:
            leftStack.append(str)
    
    
    print("".join(leftStack + rightStack[::-1]))