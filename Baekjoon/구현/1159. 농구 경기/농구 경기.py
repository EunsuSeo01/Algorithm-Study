# 농구 경기 - 브론즈 2
import sys
name_list = []
num_list = []
N = int(sys.stdin.readline().strip())
for _ in range(N):
    name = sys.stdin.readline().strip()
    try:
        # 입력받은 적 있는 성이면 개수 +1
        index = name_list.index(name[0])
        num_list[index] += 1
    except ValueError as e:
        # 처음 입력받는 성이면 리스트에 추가
        name_list.append(name[0])
        num_list.append(1)
answer = ""
for i in range(len(num_list)):
    # 5번 이상 나온 성만 answer에 추가
    if num_list[i] > 4:
        answer += name_list[i]
if len(answer) == 0:
    print("PREDAJA")
else:
    sorted_answer = ""
    for a in sorted(answer):
        sorted_answer += a
    print(sorted_answer)
