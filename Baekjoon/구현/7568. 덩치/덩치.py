# 덩치 - 실버 5
import sys

N = int(sys.stdin.readline().strip())
two_list = []
answer = []
for _ in range(N):
    xy_list = list(map(int, sys.stdin.readline().strip().split()))
    two_list.append(xy_list)
    answer.append(1)
for i in range(N):
    for j in range(N):
        if i != j:
            if two_list[i][0] > two_list[j][0] and two_list[i][1] > two_list[j][1]:
                answer[j] += 1
print(*answer)
