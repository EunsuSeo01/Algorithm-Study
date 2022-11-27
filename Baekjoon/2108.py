# 통계학
import sys
N = int(sys.stdin.readline().strip())
num_list = []
freq_list = [0 for _ in range(8002)]

# 개수만큼 숫자 입력 받기
for _ in range(N):
    n = int(sys.stdin.readline().strip())
    num_list.append(n)
    # 최빈값을 구하기 위해 인덱스별로 등장한 횟수 count 하기
    # 인덱스 1~4000는 음수(-4000~-1)의 등장 횟수, 인덱스 4001은 0의 등장 횟수, 인덱스 4002~8001는 양수(1~4000)의 등장 횟수이다
    freq_list[n + 4001] += 1

num_list.sort(reverse=True)  # 내림차순 정렬 -> 첫번째 인덱스가 최댓값
list_len = len(num_list)

print(round(sum(num_list) / list_len))  # 산술 평균
print(num_list[list_len // 2])  # 중앙값

# 최빈값 구하기
max_num = max(freq_list)
# 최빈값이 여러개일 경우 -> 최빈값 중 두번째로 작은 값을 출력해야 함
if freq_list.count(max_num) > 1:
    # 맨 처음에 등장한 값(가장 작은 최빈값)을 무시
    freq_list[freq_list.index(max_num)] = -1
    print(freq_list.index(max_num) - 4001)
# 최빈값이 1개일 때
else:
    print(freq_list.index(max_num) - 4001)

print(num_list[0] - num_list[list_len - 1])  # 범위
