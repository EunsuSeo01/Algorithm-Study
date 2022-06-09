import sys
c = int(input())
for i in range(c) :
    line = list(map(int, sys.stdin.readline().split()))
    avg = sum(line[1:]) / line[0]
    count = 0
    for j in range(1, len(line)) :
        if line[j] > avg :
            count += 1
    print("%.3f%%" %(count/line[0]*100))
