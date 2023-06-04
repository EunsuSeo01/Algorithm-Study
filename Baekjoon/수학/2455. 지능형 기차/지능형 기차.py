# 지능형 기차 - 브론즈 3
import sys
total_num = 0
max_num = 0
for _ in range(4):
    out_num, in_num = map(int, sys.stdin.readline().strip().split())
    total_num -= out_num
    total_num += in_num
    if max_num < total_num:
        max_num = total_num
print(max_num)