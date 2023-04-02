# 좌표 압축
import sys

N = int(sys.stdin.readline().strip())
li = list(map(int, sys.stdin.readline().strip().split()))

# 1. input list를 오름차순으로 정렬된 집합으로 만들기
sorted_set = sorted(set(li))

# 2. 어떤 수가 몇 번째 인덱스에 있는지(= 그 숫자보다 작은 수개 몇 개인지) 딕셔너리에 저장
dic = {}
icr = 0
for i in sorted_set:
    dic[i] = icr
    icr += 1

# 3. li 순서대로 딕셔너리에 있는 값을 key로 바로 꺼내서 출력
for i in li:
    print(dic[i], end=' ')

