# 부호 - 브론즈 3
import sys
for _ in range(3):
    N = int(sys.stdin.readline().strip())
    sum = 0
    for _ in range(N):
        sum += int(sys.stdin.readline().strip())
    if sum == 0:
        print(0)
    elif sum > 0:
        print("+")
    else:
        print("-")