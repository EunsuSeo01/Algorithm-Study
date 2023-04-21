# 집 주소 - 브론즈 3
import sys
while True:
    # 경계와 숫자 사이의 간격(좌우 총 2cm)으로 초기값을 설정
    width = 2
    nums = sys.stdin.readline().strip()
    # 각 숫자 사이의 1cm 여백 추가
    width += len(nums) - 1
    # 0이면 종료
    if nums == '0':
        break
    # 각 자리를 확인하면서 해당하는 cm만큼 추가
    for n in nums:
        if n == '1':
            width += 2
        elif n == '0':
            width += 4
        else:
            width += 3
    print(width)