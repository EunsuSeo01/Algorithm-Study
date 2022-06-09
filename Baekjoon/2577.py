import sys

mul = 1
for i in range(3) :
    n = int(sys.stdin.readline())
    mul *= n
    
string = str(mul)
for i in range(10) :
    cnt = 0
    for j in range(len(string)) :
        if i == int(string[j]) :
            cnt += 1
    print(cnt)
    
