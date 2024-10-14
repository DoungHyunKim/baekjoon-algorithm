import sys
input = lambda: sys.stdin.readline().rstrip()

# 초기 문자열을 왼쪽 스택에 저장
left_stack = list(input())
right_stack = []
repeat = int(input())

for _ in range(repeat):
    command = input().split()
    
    if command[0] == "L":  # 커서를 왼쪽으로 한 칸 이동
        if left_stack:
            right_stack.append(left_stack.pop())
    elif command[0] == "D":  # 커서를 오른쪽으로 한 칸 이동
        if right_stack:
            left_stack.append(right_stack.pop())
    elif command[0] == "B":  # 커서 왼쪽에 있는 문자 삭제
        if left_stack:
            left_stack.pop()
    elif command[0] == "P":  # 커서 왼쪽에 문자를 추가
        left_stack.append(command[1])

# 최종 출력: 왼쪽 스택 + 오른쪽 스택을 뒤집어서 출력
print("".join(left_stack + right_stack[::-1]))