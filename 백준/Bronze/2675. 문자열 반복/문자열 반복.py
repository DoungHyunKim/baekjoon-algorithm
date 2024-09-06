n = int(input())

for i in range(n):
    num, word = input().split()
    for j in range(len(word)):
        print(word[j] * int(num), end='')
    print()