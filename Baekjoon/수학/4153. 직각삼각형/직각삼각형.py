# 직각삼각형 - 브론즈 3
import sys

while True:
    a, b, c = map(int, sys.stdin.readline().strip().split())
    if a == 0 and b == 0 and c == 0:
        break
    else:
        if a**2 + b**2 == c**2:
            print("right")
        elif a**2 + c**2 == b**2:
            print("right")
        elif b**2 + c**2 == a**2:
            print("right")
        else:
            print("wrong")