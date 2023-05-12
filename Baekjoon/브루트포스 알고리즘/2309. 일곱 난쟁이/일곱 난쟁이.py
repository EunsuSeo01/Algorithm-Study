# 일곱 난쟁이 - 브론즈 1
import sys

heights = []
for _ in range(9):
    heights.append(int(sys.stdin.readline().strip()))

isEnded = False
# 전체 sum - 2명의 난쟁이 키 = 100
for i in range(8):
    for j in range(i + 1, 9):
        if sum(heights) - heights[i] - heights[j] == 100:
            heights[i] = 0
            heights[j] = 0
            isEnded = True
            break
    if isEnded:
        break
heights.sort()
for height in heights:
    if height != 0:
        print(height)
