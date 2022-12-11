# 블랙잭 - 브론즈 2
import sys

N, M = map(int, sys.stdin.readline().strip().split())
numbers = sys.stdin.readline().strip().split()
li = []

for i in range(N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            res = int(numbers[i]) + int(numbers[j]) + int(numbers[k])
            if M >= res:
                li.append(res)

print(max(li))
