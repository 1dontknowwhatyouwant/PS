import sys
input = sys.stdin.readline

def backtracking(nums, target, index=0, current_sum=0):
    global count
    if index == len(nums):
        return
    if current_sum + nums[index] == target:
        count += 1
    
    backtracking(nums, target, index + 1, current_sum + nums[index])
    backtracking(nums, target, index + 1, current_sum)

input = sys.stdin.readline
N, S = map(int, input().split())
num = list(map(int, input().split()))
count = 0

backtracking(num, S)
print(count)
