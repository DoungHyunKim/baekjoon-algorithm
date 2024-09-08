def fatorial(N):
    if N == 0:
        return 1
    else:
        return N * fatorial(N-1)
    
print(fatorial(int(input())))