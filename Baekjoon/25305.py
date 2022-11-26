# 커트라인 = 상을 받는 사람들 중 최하점
# 정렬하고 k번째로 높은 사람의 점수를 출력하면 된다.
import sys

N, k = map(int, sys.stdin.readline().split(' '))
scores = map(int, sys.stdin.readline().strip().split(' '))
print(sorted(scores, reverse=True)[k - 1])
