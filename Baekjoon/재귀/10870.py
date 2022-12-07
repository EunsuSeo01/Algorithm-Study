# 피보나치 수 5 - 브론즈 2
n = int(input())


def fibonacci(n: int) -> int:
    if n == 0 or n == 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(n))
