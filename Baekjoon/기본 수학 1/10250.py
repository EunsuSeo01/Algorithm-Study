import sys

T = int(input())
for _ in range(T):
    H, W, N = map(int, sys.stdin.readline().strip().split())
    floor = N % H
    room = N // H
    if floor == 0:
        floor = H
    else:
        room += 1
    print(floor * 100 + room)
