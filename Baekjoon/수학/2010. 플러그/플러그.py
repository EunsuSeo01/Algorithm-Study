# 플러그 - 브론즈 3
import sys
N = int(sys.stdin.readline().strip())
multi_taps = []
for _ in range(N):
    multi_taps.append(int(sys.stdin.readline().strip()))
multi_taps.sort()
print(sum(multi_taps) - (len(multi_taps) - 1))
