# 괄호 - 실버 4
import sys
T = int(sys.stdin.readline().strip())
for _ in range(T):
    data = sys.stdin.readline().strip()
    # 변수값 초기화
    left = 0
    right = 0
    isFirst = True
    for d in data:
        if d == '(':
            left += 1
        else:
            # 처음 단어가 아닌 ')'
            if not isFirst:
                # '('가 앞에 없었다면 NO
                if left == 0:
                    right = -1
                    break
                # '('가 앞에 있었다면 1개 상쇄
                else:
                    left -= 1
            # 처음 단어인데 ')'라면 무조건 NO
            else:
                right = -1
                break
        isFirst = False
    if left == 0 and right == 0:
        print("YES")
    else:
        print("NO")
