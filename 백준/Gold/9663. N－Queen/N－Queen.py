def nqueen(n):
    global cnt 
    if n == N:
        cnt += 1
        return
    
    for j in range(N):
        if v1[j] == v2[n+j] == v3[n-j] == 0:
            v1[j] = v2[n+j] = v3[n-j]  = 1
            nqueen(n+1)
            v1[j] = v2[n +j] = v3[n-j] = 0

N = int(input())
v1 = [0] *N
v2 = [0] * (2*N)
v3 = [0] * (2*N)
cnt =0

nqueen(0)
print(cnt)