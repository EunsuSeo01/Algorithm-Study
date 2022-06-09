import sys
arr = []
for i in range(10) :
    n = int(sys.stdin.readline())
    n %= 42
    try:
        arr.index(n)
    except:
        arr.append(n)
        continue
print(len(arr))
