# 하얀 칸 - 브론즈 2
# 하얀 칸 위에 말이 몇 개 있는지
import sys

count = 0
# for문으로 총 8줄을 입력받는다
for i in range(1, 9):
    line = list(sys.stdin.readline().strip())
    # 짝수 줄 -> 검,하,검,하,...
    if i % 2 == 0:
        # 홀수 인덱스가 F면 count
        for j in range(1,8,2):
            if line[j] == 'F':
                count += 1
    # 홀수 줄 -> 하,검,하,검,...
    else:
        # 짝수 인덱스가 F면 count
        for j in range(0,7,2):
            if line[j] == 'F':
                count += 1

print(count)
