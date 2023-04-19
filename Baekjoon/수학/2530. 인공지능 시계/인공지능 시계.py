# 인공지능 시계 - 브론즈 4
import sys

h,m,s = map(int, sys.stdin.readline().strip().split())
cooking_seconds = int(sys.stdin.readline().strip())

s += cooking_seconds % 60
m += cooking_seconds // 60 + s // 60
h += m // 60

if h >= 24:
    h %= 24
if m >= 60:
    m %= 60
if s >= 60:
    s %= 60

print(h, m, s)
