import sys
input = lambda: sys.stdin.readline().rstrip()

def main():
    n, m = map(int, input().split())  # 배열의 크기를 나타내는 변수로 n(행), m(열)을 사용
    
    arr1 = [list(map(int, input().split())) for _ in range(n)]  # n개의 행을 가진 배열
    arr2 = [list(map(int, input().split())) for _ in range(n)]  # n개의 행을 가진 배열

    for i in range(n):  # n개의 행에 대해 반복
        for j in range(m):  # m개의 열에 대해 반복
            arr1[i][j] = arr1[i][j] + arr2[i][j]
     
    for i in range(n):
        for j in range(m):
            print(arr1[i][j], end=' ')
        print()  # 한 행을 출력한 뒤 줄바꿈 추가

if __name__ == "__main__":
    main()
