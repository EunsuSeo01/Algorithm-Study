# 슈퍼 마리오 - 브론즈 1
import sys
input_list = [int(sys.stdin.readline().strip()) for _ in range(10)]

score = 0
two = []
for i in input_list:
    score += i
    if score >= 100:
        two.append(score)
        two.append(score - i)
        break
if len(two) == 0:
    print(score)
else:
    if abs(100 - two[0]) > abs(100 - two[1]):
        print(two[1])
    elif abs(100 - two[0]) < abs(100 - two[1]):
        print(two[0])
    else:
        print(max(two))
