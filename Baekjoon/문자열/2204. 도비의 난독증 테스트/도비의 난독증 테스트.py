# 도비의 난독증 테스트 - 브론즈 1
import sys

while True:
    input_list = []
    n = int(sys.stdin.readline().strip())
    if n == 0:
        break
    for i in range(n):
        input_list.append(sys.stdin.readline().strip())
    # sort의 key를 str.lower로 설정하면 대소문자 구분없이 정렬됨
    input_list.sort(key=str.lower)
    print(input_list[0])
