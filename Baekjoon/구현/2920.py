# 음계 - 브론즈 2

numbers = list(map(int, input().split()))

case = 0
for i in range(1, len(numbers)):
    # (앞뒤 숫자의 차를 이용해) 오름차순
    if numbers[i - 1] - numbers[i] == -1:
        case = 1
    # 내림차순
    elif numbers[i - 1] - numbers[i] == 1:
        case = 2
    # 믹스
    else:
        case = 3
        break

if case == 1:
    print("ascending")
elif case == 2:
    print("descending")
elif case == 3:
    print("mixed")