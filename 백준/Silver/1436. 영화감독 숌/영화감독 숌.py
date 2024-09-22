N = int(input())

# ~665 전까지는 의미가 없으므로 666부터 시작한다.
num_of_end = 666

count = 0

while count != N:
	# num_of_end 에 666이 존재할 때, count에 1을 증가시킨다.
	if '666' in str(num_of_end):
		count += 1
    # count == N 같을 때까지 num_of_end를 1씩 증가 시킨다. 
	num_of_end += 1

print(num_of_end-1)