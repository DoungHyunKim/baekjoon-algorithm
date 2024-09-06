A = []
for _ in range(9):
    num = int(input())
    A.append(num)
index = A.index(max(A))
print(max(A))
print(index+1)