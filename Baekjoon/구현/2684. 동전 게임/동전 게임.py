# 동전 게임 - 브론즈 1
import sys
P = int(sys.stdin.readline().strip())
line = []
for i in range(P):
    answer = [0] * 8
    line.append(sys.stdin.readline().strip())
    for j in range(38):
        if line[i][j] == 'T' and line[i][j + 1] == 'T' and line[i][j + 2] == 'T':
            answer[0] += 1
        elif line[i][j] == 'T' and line[i][j + 1] == 'T' and line[i][j + 2] == 'H':
            answer[1] += 1
        elif line[i][j] == 'T' and line[i][j + 1] == 'H' and line[i][j + 2] == 'T':
            answer[2] += 1
        elif line[i][j] == 'T' and line[i][j + 1] == 'H' and line[i][j + 2] == 'H':
            answer[3] += 1
        elif line[i][j] == 'H' and line[i][j + 1] == 'T' and line[i][j + 2] == 'T':
            answer[4] += 1
        elif line[i][j] == 'H' and line[i][j + 1] == 'T' and line[i][j + 2] == 'H':
            answer[5] += 1
        elif line[i][j] == 'H' and line[i][j + 1] == 'H' and line[i][j + 2] == 'T':
            answer[6] += 1
        elif line[i][j] == 'H' and line[i][j + 1] == 'H' and line[i][j + 2] == 'H':
            answer[7] += 1
    for a in answer:
        print(a, end=' ')
    print()
    answer.clear()