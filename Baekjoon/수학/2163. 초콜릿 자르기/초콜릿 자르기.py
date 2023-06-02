# 초콜릿 자르기 - 브론즈 1
import sys

N, M = map(int, sys.stdin.readline().strip().split())
print(N - 1 + (M - 1) * N)
