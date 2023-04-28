# 세준세비 - 1524번
import sys
T = int(sys.stdin.readline().strip())

for _ in range(T):
    S_index = 0
    B_index = 0
    # 줄바꿈으로 구분
    empty = sys.stdin.readline()
    N, M = map(int, sys.stdin.readline().strip().split())
    S = list(map(int, sys.stdin.readline().strip().split()))
    B = list(map(int, sys.stdin.readline().strip().split()))
    # 힘의 순서대로 정렬
    S.sort()
    B.sort()
    # S와 B에 남은 병사들이 없을 때까지 반복
    while len(S) != 0 and len(B) != 0:
        # S 힘이 세면 B의 병사 죽음
        if S[0] > B[0]:
            B.remove(B[0])
        # B 힘이 세면 S의 병사 죽음
        elif S[0] < B[0]:
            S.remove(S[0])
        # 힘이 같으면 B의 병사 죽음
        else:
            B.remove(B[0])
    if len(B) == 0:
        print("S")
    elif len(S) == 0:
        print("B")
    else:
        print("C")