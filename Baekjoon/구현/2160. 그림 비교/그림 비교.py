# 그림 비교 - 브론즈 1
import sys
N = int(sys.stdin.readline().strip())
drawings = [''] * N
for n in range(N):
    for _ in range(5):
        drawings[n] += (sys.stdin.readline().strip())

target_d1 = 1
target_d2 = 2
cnt_sum = 35
for i in range(N-1):
    for j in range(i+1, N):
        cnt = 0
        for k in range(5*7):
            if drawings[i][k] != drawings[j][k]:
                cnt += 1
        if cnt_sum > cnt:
            target_d1 = i + 1
            target_d2 = j + 1
            cnt_sum = cnt
print(target_d1, target_d2)
