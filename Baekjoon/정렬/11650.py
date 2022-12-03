# 좌표 정렬하기
import sys

N = int(sys.stdin.readline().strip())
li = []
for i in range(N):
    x, y = map(int, sys.stdin.readline().strip().split(' '))
    li.append([x,y])
li.sort()
for x,y in li:
    print(x, y)