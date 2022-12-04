# 나이순 정렬
import sys

N = int(sys.stdin.readline().strip())
li = []
for i in range(N):
    age, name = sys.stdin.readline().split()
    li.append([int(age), name])
# 2중 리스트일 때 첫 번째 원소인 age를 기준으로 정렬 -> age가 같으면 list에 append된 순서대로 출력된다
li.sort(key=lambda x: x[0])
for age, name in li:
    print(age, name)
