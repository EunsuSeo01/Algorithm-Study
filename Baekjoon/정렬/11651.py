# 좌표 정렬하기 2
import sys

N = int(sys.stdin.readline().strip())
li = []
for i in range(N):
    x, y = map(int, sys.stdin.readline().strip().split(' '))
    # 앞에 들어가는 값 기준으로 정렬되기 때문에 y를 앞쪽에 두고 이어붙인다.
    li.append([y, x])
li.sort()
for y, x in li:
    print(x, y)
