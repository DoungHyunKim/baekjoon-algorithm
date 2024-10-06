import sys
input = sys.stdin.readline

def dfs(n, temp, lst, operators, N, mx, mn):
    # 종료 조건
    if n == N-1:
        mx[0] = max(temp, mx[0])
        mn[0] = min(temp, mn[0])
        return
    
    # 하부함수 호출
    if operators[0] != 0:  # 덧셈하는 경우
        operators[0] -= 1
        dfs(n+1, temp + lst[n+1], lst, operators, N, mx, mn)
        operators[0] += 1

    if operators[1] != 0:  # 뺄셈하는 경우
        operators[1] -= 1
        dfs(n+1, temp - lst[n+1], lst, operators, N, mx, mn)
        operators[1] += 1

    if operators[2] != 0:  # 곱셈하는 경우
        operators[2] -= 1
        dfs(n+1, temp * lst[n+1], lst, operators, N, mx, mn)
        operators[2] += 1

    if operators[3] != 0:  # 나눗셈하는 경우
        operators[3] -= 1
        dfs(n+1, int(temp / lst[n+1]), lst, operators, N, mx, mn)
        operators[3] += 1

def main():
    N = int(input())  # 숫자의 개수

    lst = list(map(int, input().split()))  # 숫자 리스트

    operators = list(map(int, input().split()))  # 연산자 리스트

    mx = [-int(1e9)]  # 최댓값 (리스트로 감싸서 참조할 수 있게 처리)
    mn = [int(1e9)]  # 최솟값

    dfs(0, lst[0], lst, operators, N, mx, mn)  # 첫 번째 숫자로 시작

    print(mx[0])
    print(mn[0])

if __name__ == "__main__":
    main()
