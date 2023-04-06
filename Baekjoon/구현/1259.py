# 팰린드롬수 - 브론즈 1
import sys

while True:
    nums = list(map(int, sys.stdin.readline().strip()))
    # 숫자가 1개일 때 판단
    if len(nums) == 1:
        # 그 1개의 숫자가 0이면 종료
        if nums[0] == 0:
            break
        # 아니면 팰린드롬수 맞음
        else:
            print("yes")
    # 숫자가 2개 이상일 때 판단
    else:
        # 2로 나눠서 중간 인덱스 파악
        half = len(nums) // 2
        isEnded = False
        # 중간 지점 기준으로 양쪽 숫자들 좁혀오면서 서로 일치하는지 확인
        for i in range(half):
            # 팰린드롬수 아닐 경우 -> isEnded로 표시하고 break으로 for문 바로 탈출
            if nums[i] != nums[len(nums) - 1 - i]:
                isEnded = True
                break
        if isEnded:
            print("no")
        else:
            print("yes")