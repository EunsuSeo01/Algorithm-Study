# 요세푸스 문제 0 - 실버 5
N, K = map(int, input().split())

nums = [n for n in range(1, N + 1)]
answer = []

# 삭제할 인덱스
index = K - 1
# 최대 인덱스
max = len(nums) - 1

# 삭제도 N번 진행하게 됨
for i in range(N):
    # 삭제될 숫자
    num = nums[index]
    nums.remove(num)
    # 정답 리스트에 추가
    answer.append(num)
    # 삭제할 인덱스, 최대 인덱스 업데이트
    index += K - 1
    max -= 1
    # nums에 남은 숫자가 1개면 정답에 추가하고 끝
    if max == 0:
        answer.append(nums[0])
        break
    # nums에 남은 숫자가 없으면 바로 끝
    elif max < 0:
        break
    # nums에 남은 숫자가 2개 이상이고, index가 max 넘어가면 % 연산을 통해 앞의 인덱스로 넘어간다
    elif index > max:
        index %= max + 1

# 정답 형식으로 print
print("<", end='')
now = 0
for a in answer:
    if now == len(answer) - 1:
        print(f"{a}", end='>')
    else:
        print(f"{a},", end=' ')
    now += 1