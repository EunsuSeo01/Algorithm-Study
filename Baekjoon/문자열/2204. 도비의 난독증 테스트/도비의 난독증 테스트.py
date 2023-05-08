# 도비의 난독증 테스트 - 브론즈 1
import sys

while True:
    input_list = []  # 원본 인풋 리스트
    input_dict = {}  # 인풋의 소문자와 인덱스를 담고 있는 딕셔너리
    sorted_list = []  # 정렬된 인풋 리스트
    n = int(sys.stdin.readline().strip())
    if n == 0:
        break
    for i in range(n):
        input_str = sys.stdin.readline().strip()
        input_list.append(input_str)
        # 소문자로 변환해서 딕셔너리에 인덱스와 함께 저장
        input_dict[input_str.lower()] = i
    # 정렬
    sorted_list = sorted(input_dict)
    # 정렬된 리스트 중 첫번째 원소의 인덱스를 딕셔너리에서 얻어서 원본 리스트에서 찾는다
    print(input_list[input_dict.get(sorted_list[0])])
