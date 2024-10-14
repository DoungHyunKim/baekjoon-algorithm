import sys
input = lambda: sys.stdin.readline().rstrip()

# 건물의 개수 입력
N = int(input())
# 각 건물의 높이를 입력받음
building_heights = [int(input()) for _ in range(N)]

stack = []
result = 0

for building_height in building_heights:
    # 현재 건물 높이보다 같거나 낮은 건물들은 스택에서 제거
    while stack and stack[-1] <= building_height:
        stack.pop()
    
    # 현재 건물은 스택에 추가
    stack.append(building_height)
    
    # 스택에 남아있는 건물들은 현재 건물보다 높은 건물들이므로
    # 자기 자신을 제외한 나머지를 결과에 더함
    result += len(stack) - 1

print(result)
