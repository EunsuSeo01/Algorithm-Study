# 핸드폰 요금 - 브론즈 3
import sys

N = int(sys.stdin.readline().strip())
T = list(map(int, sys.stdin.readline().strip().split()))
Y = 0
M = 0

# 각 요금제 썼을 때의 총 요금 계산
for n in T:
    Y += ((n // 30) + 1) * 10
    M += ((n // 60) + 1) * 15

if Y < M:
    print("Y", Y)
elif M < Y:
    print("M", M)
else:
    print("Y", "M", Y)