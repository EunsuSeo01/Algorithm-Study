# 나누기 - 브론즈 2
import sys

N = int(sys.stdin.readline().strip())
F = int(sys.stdin.readline().strip())
divisor = 100

# 마지막 2자리를 0으로 만든다
N -= N % divisor

while True:
    if N % F == 0:
        break
    N += 1

N = str(N)
print(N[len(N) - 2] + N[len(N)-1])
