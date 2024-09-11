import sys

def josep(N,K):
    people = list(range(1,N+1))
    index = 0
    result = []
    while len(people) > 1:
        index = (index + K - 1) % len(people)
        result.append(people.pop(index))
    
    result.append(people[0])
    
    print('<'+ ', '.join(map(str, result)) + '>')

N, K = map(int, input().split())

josep(N, K)