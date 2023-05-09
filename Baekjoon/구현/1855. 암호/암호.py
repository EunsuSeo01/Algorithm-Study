# 암호 - 브론즈 1
import sys

K = int(sys.stdin.readline().strip())
encrypt = sys.stdin.readline().strip()
row = int(len(encrypt) / K)
original = []

for i in range(row):
    row_list = []
    if i % 2 == 0:
        # 0 1 2 / 6 7 8
        for j in range(i * K, (i + 1) * K):
            row_list.append(encrypt[j])
        original.append(row_list)
    else:
        # i = 1 / 5 4 3
        # i = 3 / 11 10 9
        for j in range(K * (i + 1) - 1, K * i - 1, -1):
            row_list.append(encrypt[j])
        original.append(row_list)

# 다른 행 같은 열 print
for c in range(K):
    for r in range(row):
        print(original[r][c], end='')
