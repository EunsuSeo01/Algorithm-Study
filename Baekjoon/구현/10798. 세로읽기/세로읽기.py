# 세로읽기 - 10798번
import sys
data = ['' * 15] * 5
max_len = 0
for i in range(5):
    data[i] = sys.stdin.readline().strip()
    if max_len < len(data[i]):
        max_len = len(data[i])
for c in range(max_len):
    for r in range(5):
        try:
            print(data[r][c], end='')
        except IndexError:
            continue
            