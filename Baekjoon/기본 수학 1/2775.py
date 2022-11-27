import sys

apart = [[-1 for col in range(15)] for row in range(15)]


def count_people(k: int, n: int) -> int:
    answer = 0
    if apart[k][n] == -1:
        if k == 0:
            return n
        else:
            for i in range(1, n + 1):
                answer += count_people(k - 1, i)
        apart[k][n] = answer
    else:
        answer = apart[k][n]
    return answer


T = int(input())
for _ in range(T):
    k = int(sys.stdin.readline().strip())
    n = int(sys.stdin.readline().strip())
    print(count_people(k, n))
