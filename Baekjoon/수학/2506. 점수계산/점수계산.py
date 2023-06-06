# 점수계산 - 브론즈 3
import sys
N = int(sys.stdin.readline().strip())
score = 0
plus = 0
input_list = list(map(int, sys.stdin.readline().strip().split()))
for num in input_list:
    if num == 0:
        plus = 0
    else:
        plus += 1
        score += plus
print(score)
