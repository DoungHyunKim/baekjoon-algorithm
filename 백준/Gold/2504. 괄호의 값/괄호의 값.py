import sys
input = lambda: sys.stdin.readline().strip()

def calculate(s):
    sum = 0
    multi = 1
    stack = []

    for i in range(len(s)):
        if s[i] == "(":
            stack.append("(")
            multi *= 2
        elif s[i] == "[":
            stack.append("[")
            multi *= 3
        elif s[i] == ")":
            if not stack or stack[-1] != "(":
                return 0
            if s[i - 1] == "(":
                sum += multi
            stack.pop()
            multi //= 2
        elif s[i] == "]":
            if not stack or stack[-1] != "[":
                return 0
            if s[i - 1] == "[":
                sum += multi
            stack.pop()
            multi //= 3

    return sum if not stack else 0

if __name__ == "__main__":
    line = input()
    print(calculate(line))
