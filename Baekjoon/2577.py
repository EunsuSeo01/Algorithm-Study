import sys
mul = 1
arr = []
digit = 10
for i in range(3) :
    n = int(sys.stdin.readline())
    mul *= n
print(mul)
for j in range(len(str(mul))) :
    arr.append(mul % digit)
    digit *= 10
print(arr)
    
