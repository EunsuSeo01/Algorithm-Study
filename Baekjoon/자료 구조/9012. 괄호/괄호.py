# 괄호 - 실버 4
import sys
T = int(sys.stdin.readline().strip())
for _ in range(T):
    data = sys.stdin.readline().strip()
    left = 0
    right = 0
    isFirst = True
    for d in data:
        if d == '(':
            left += 1
        else:
            if not isFirst:
                if left == 0:
                    right += 1
                else:
                    left -= 1
            else:
                right = -1
                break
        isFirst = False
    if left == 0 and right == 0:
        print("YES")
    else:
        print("NO")
