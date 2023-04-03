# 칸토어 집합 - 실버 3
import sys


def divideToThree(n: int, start: int, end: int):
    # 탈출
    if n == 0:
        return
    else:
        # 3등분 시 부분이
        count = (end - start + 1) // 3
        # 왼쪽 재귀
        divideToThree(n - 1, start, start + count - 1)
        # 가운데 공백 처리
        for i in range(start + count, start + count * 2):
            answer[i] = ' '
        # 오른쪽 재귀
        divideToThree(n - 1, start + count * 2, start + count * 3 - 1)


while True:
    try:
        N = int(sys.stdin.readline())
        # 문자열 생성
        answer = ['-'] * (3 ** N)
        # 재귀 함수 실행
        divideToThree(N, 0, 3 ** N - 1)
        print(''.join(answer))
    except:
        break
