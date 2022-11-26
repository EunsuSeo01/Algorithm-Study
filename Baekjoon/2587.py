# 대표값2
import sys
n = []
for _ in range(5):
    n.append(int(sys.stdin.readline().strip()))

print(int(sum(n) / 5))
print(sorted(n)[2])
