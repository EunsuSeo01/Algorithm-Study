# 공 - 브론즈 3
import sys
M = int(sys.stdin.readline().strip())
cup_nums = [1, 2, 3]

for _ in range(M):
    X, Y = map(int, sys.stdin.readline().strip().split())
    x_index = cup_nums.index(X)
    y_index = cup_nums.index(Y)
    temp = cup_nums[x_index]
    cup_nums[x_index] = cup_nums[y_index]
    cup_nums[y_index] = temp
print(cup_nums[0])
