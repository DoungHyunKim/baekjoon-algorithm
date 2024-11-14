n = int(input())

for i in range(1, n + 1):
    clap = str(i).count('3')
    clap += str(i).count('6')
    clap += str(i).count('9')
    
    if clap != 0:
        print(clap *'-', end=' ')
    else:
        print(i, end=' ')