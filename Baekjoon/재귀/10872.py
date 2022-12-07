# 팩토리얼 - 브론즈 5
N = int(input())


def factorial(n: int) -> int:
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


print(factorial(N))
