# 카드2 - 실버 4
N = int(input())
nums = list(range(1, N+1))

# 처리 순서 (현재 1번째)
turn = 1
top_index = 0
bottom_index = len(nums) - 1

# 첫번째 인덱스와 마지막 인덱스가 같으면 종료 = 원소가 1개 남은 경우
while top_index != bottom_index:
    # 짝수번째 차례일 경우 맨 위의 카드를 맨 아래로 이동
    if turn % 2 == 0:
        nums.append(nums[top_index])
        bottom_index += 1
    top_index += 1
    turn += 1

print(nums[bottom_index])
