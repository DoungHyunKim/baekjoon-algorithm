N, K = map(int, input().split())

students = [[0]* 6 for _ in range(2)]  # 2 x 6 배열, [성별][학년]

for i in range(N):
    gender, grade = map(int, input().split())
    students[gender][grade-1] += 1  # 성별과 학년별 학생 수 카운트

rooms = 0

for gender in range(2):
    for grade in range(6):
        if students[gender][grade] > 0:
            # 방의 수 계산, 올림 처리로 (학생 수 + K - 1) // K 사용
            rooms += (students[gender][grade] + K - 1) // K

print(rooms)
