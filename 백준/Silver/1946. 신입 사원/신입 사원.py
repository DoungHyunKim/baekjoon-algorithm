import sys
input = sys.stdin.readline

def count_successful_candidates(candidates):
    candidates.sort()  # 서류 점수 기준으로 정렬
    max_interview_score = float('inf')
    successful_count = 0

    for _, interview_score in candidates:
        if interview_score < max_interview_score:
            max_interview_score = interview_score
            successful_count += 1

    return successful_count

def main():
    test_case = int(input())

    for _ in range(test_case):
        num_candidates = int(input())
        candidates = [tuple(map(int, input().split())) for _ in range(num_candidates)]
        print(count_successful_candidates(candidates))

if __name__ == "__main__":
    main()
