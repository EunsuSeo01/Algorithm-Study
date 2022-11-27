A, B, C = map(int, input().split())
N = -1
if B != C:
    sub = A / (C - B)
    if sub > 0:
        N = int(sub + 1)
print(N)
