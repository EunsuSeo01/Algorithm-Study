# 가장 큰 금민수 - 브론즈 1
import sys
N = int(sys.stdin.readline().strip())
num = 4
max_num = num
while num <= N:
    if not ('0' in str(num) or '1' in str(num) or '2' in str(num) or '3' in str(num) or '5' in str(num) or '6' in str(num) or '8' in str(num) or '9' in str(num)):
        if max_num < num:
            max_num = num
    num += 1
print(max_num)