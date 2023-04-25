# 저항 - 브론즈 2
import sys

registers = ["black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"]
inputs = [sys.stdin.readline().strip() for _ in range(3)]

values = registers.index(inputs[0]) * 10 + registers.index(inputs[1])
# 곱할 값(마지막 색)은 10의 인덱스 승 하면 나온다
values *= 10 ** registers.index(inputs[2])
print(values)