# 수 정렬하기 3 - 브론즈 1
import sys

N = int(sys.stdin.readline().strip())

# 미리 최대 범위까지 고려해서 0으로 채워진 리스트를 만들어둔다.
li = [0] * 10001

# N개의 입력값을 받는다.
for _ in range(N):
    num = int(sys.stdin.readline().strip())
    # 받은 입력값 만큼의 위치에(인덱스에) +1 -> 해당 인덱스 값이 몇번 입력됐는지 개수가 저장된다.
    li[num] += 1

for i in range(len(li)):
    # 리스트를 순회하면서 입력값으로 들어온 인덱스만 확인한다.
    # -> 인덱스 순서로 순회하기 때문에 자동으로 오름차순으로 확인하게 된다. => 이 점을 활용하는 게 이 문제의 키포인트!
    if li[i] != 0:
        # 입력된 횟수만큼 반복문을 돌려서 인덱스 값을 출력한다.
        for _ in range(li[i]):
            print(i)