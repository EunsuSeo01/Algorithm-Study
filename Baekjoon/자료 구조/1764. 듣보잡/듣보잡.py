# 듣보잡 - 실버 4
import sys

N, M = map(int, sys.stdin.readline().strip().split())
people = []
answer = []

# 듣도 못한 사람, 보도 못한 사람 저장
for _ in range(N+M):
    people.append(sys.stdin.readline().strip())
# 집합 자료구조로 만들어서 중복 제거
set_peole = set(people)

for p in people:
    # p가 set_people에 없으면 중복인 것
    if p not in set_peole:
        answer.append(p)
    # p가 set_people에 있으면 삭제
    else:
        set_peole.remove(p)

# 사전순 정렬
answer.sort()
print(len(answer))
for a in answer:
    print(a)
    