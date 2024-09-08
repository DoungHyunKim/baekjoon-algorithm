def hanoi (N, start, end, mid):
    if(N <= 20):
        if N == 1: 
            print(start, end)  # base case
            return 
        else:
            hanoi(N-1,start, mid, end)
            print(start,end)
            hanoi(N-1, mid, end, start)
    else:
        return

N = int(input())
print(2**N-1)

hanoi(N,1,3,2)