# 수 정렬하기 2
# 오름차순 정렬
import sys

nums = []
N = int(sys.stdin.readline().strip())
for _ in range(N):
    nums.append(int(sys.stdin.readline().strip()))
nums.sort()
for i in nums:
    print(i)