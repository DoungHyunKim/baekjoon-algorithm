def is_balanced(s):
    stack = []
    for char in s:
        if char == '(' or char == '[':
            stack.append(char)
        elif char == ')':
            if not stack or stack[-1] != '(':
                return False
            stack.pop()
        elif char == ']':
            if not stack or stack[-1] != '[':
                return False
            stack.pop()
    return len(stack) == 0

while True:
    line = input().rstrip()
    if line == '.':
        break
    if is_balanced(line):
        print("yes")
    else:
        print("no")
