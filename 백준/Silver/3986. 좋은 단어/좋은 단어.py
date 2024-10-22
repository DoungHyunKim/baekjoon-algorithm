import sys
input = lambda: sys.stdin.readline().rstrip()

def is_good(s):
    stack = []

    for char in s:
        if stack and stack[-1] == char:
            # 스택의 최상단과 같은 문자가 있으면 pop
            stack.pop()
        else:
            # 그렇지 않으면 스택에 push
            stack.append(char)

    # 스택이 비어있으면 좋은 단어 (모든 문자가 짝을 이룸)
    return 1 if not stack else 0

N = int(input())  # 입력 문자열의 개수
result = 0

for _ in range(N):
    line = input()
    result += is_good(line)

print(result)
