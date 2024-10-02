import sys
input = lambda: sys.stdin.readline().rstrip()

test_case = int(input())

def employment(candidate):
    maginot_line = sys.maxsize
    successful_candidate = 0

    candidate = sorted(candidate, key=lambda x: (x[1], x[0]))
    for document_score, interview_score in candidate:
        if document_score < maginot_line:
            maginot_line = document_score
            successful_candidate += 1
    return successful_candidate


for _ in range(test_case):
    total_candidate = int(input())
    candidate_list = []
    for _ in range(total_candidate):
        candidate_list.append(list(map(int, input().split())))
    print(employment(candidate_list))
