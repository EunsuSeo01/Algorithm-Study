# 분산처리 - 브론즈 2
import sys

T = int(sys.stdin.readline().strip())
for _ in range(T):
    a, b = map(int, sys.stdin.readline().strip().split())
    if a % 10 == 0:
        print("10")
    elif b % 4 == 0:
        print(a ** 4 % 10)
    else:
        b %= 4
        print(a ** b % 10)