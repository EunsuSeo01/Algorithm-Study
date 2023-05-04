# 수열의 변화 - 브론즈 1
import sys

N, K = map(int, sys.stdin.readline().strip().split())
nums = list(map(int, sys.stdin.readline().strip().split(',')))

for _ in range(K):
    answer = []
    for i in range(len(nums)-1):
        answer.append(nums[i+1] - nums[i])
    nums = answer

turn = 0
for i in nums:
    if turn == len(nums)-1:
        print(i)
    else:
        print(i, end=',')
    turn += 1
