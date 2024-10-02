import sys
input = lambda: sys.stdin.readline().rstrip()

def max_sum(nums, N):
    for i in range(1, N):
        nums[i] = max(nums[i], nums[i-1] + nums[i])
    
    return max(nums)

def main():
    N = int(input())
    nums = list(map(int, input().split()))
    print(max_sum(nums, N))

if __name__ == "__main__":
    main()