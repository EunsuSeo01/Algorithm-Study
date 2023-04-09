# 이항 계수 1 - 브론즈 1
N, K = map(int, input().split())

def factorial(n: int) -> int:
    # K는 0이 올 수 있고, 0!은 1이기 때문이다
    if n == 0:
        return 1
    elif n == 1:
        return n
    else:
        return n * factorial(n - 1)

print(int(factorial(N)/(factorial(K) * factorial(N-K))))