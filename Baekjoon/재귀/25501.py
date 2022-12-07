# 재귀의 귀재 - 브론즈 2
import sys

# 전역변수 선언
global count


def recursion(s: str, start: int, end: int) -> int:
    global count
    count += 1
    if start >= end:
        return 1
    elif s[start] != s[end]:
        return 0
    else:
        return recursion(s, start+1, end-1)


def isPalindrome(s: str) -> [int]:
    return recursion(s, 0, len(s)-1)


N = int(sys.stdin.readline().strip())
for _ in range(N):
    count = 0
    string = sys.stdin.readline().strip()
    print(isPalindrome(string), count)
    