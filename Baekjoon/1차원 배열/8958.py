import sys
T = int(input())
for i in range(T) :
    score = 0
    total = 0
    line = sys.stdin.readline().strip()
    for j in range(len(line)) :
        if line[j] == "O" :
            score += 1
            total += score
        else :
            score = 0
    print(total)
