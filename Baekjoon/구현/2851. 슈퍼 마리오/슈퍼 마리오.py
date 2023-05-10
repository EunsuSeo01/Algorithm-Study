# 슈퍼 마리오 - 브론즈 1
import sys
input_list = [int(sys.stdin.readline().strip()) for _ in range(10)]

score = 0
for i in input_list:
    score += i
    if score == 100:
        break
    elif score > 100:
        if score - 100 > 100 - (score - i):
            score -= i
        else:
            break
        break
print(score)
