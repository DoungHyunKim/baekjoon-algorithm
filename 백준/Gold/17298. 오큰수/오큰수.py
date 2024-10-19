import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
NGE = list(map(int, input().split()))

result = [-1] * N  # 결과를 저장할 리스트를 -1로 초기화
stack = []  # 스택을 초기화

for i in range(N):
    # 현재 수가 스택의 가장 위의 수보다 크면
    while stack and NGE[stack[-1]] < NGE[i]:
        index = stack.pop()  # 인덱스를 스택에서 꺼내고
        result[index] = NGE[i]  # 결과 리스트에 다음 큰 수 저장
    stack.append(i)  # 현재 인덱스를 스택에 추가

print(' '.join(map(str, result)))