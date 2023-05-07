# 쉽게 푸는 문제 - 브론즈 1
import sys

# 조건의 범위만큼 미리 리스트를 채우기
num_list = []
num = 0
while len(num_list) <= 1000:
    for _ in range(num):
        num_list.append(num)
    num += 1

A, B = map(int,sys.stdin.readline().strip().split())
# 입력받은 범위의 숫자의 합 출력
print(sum(num_list[A-1:B]))
