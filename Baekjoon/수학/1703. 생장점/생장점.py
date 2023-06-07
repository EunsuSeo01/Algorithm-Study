# 생장점 - 브론즈 3
import sys
while True:
    answer = 1
    line = sys.stdin.readline().strip()
    if line == '0':
        break
    else:
        line = list(map(int, line.split()))
        for i in range(1, len(line), 2):
            answer *= line[i]
            answer -= line[i + 1]
    print(answer)
    