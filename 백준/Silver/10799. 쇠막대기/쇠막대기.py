def count_stick(s):
    stack = []
    result = 0

    for i in range(len(s)):
        if s[i] == '(':
            stack.append('(')
        else:
            if s[i-1] == '(': # 레이저
                stack.pop()
                result += len(stack)
            else:
                stack.pop()
                result += 1
    print(result)

count_stick(input())

