import sys

numbers = []
for i in range(9):
    numbers.append(list(map(int, sys.stdin.readline().strip().split(' '))))

max = -1
for i in range(9):
    for j in range(9):
        if max < numbers[i][j]:
            max = numbers[i][j]
            row = i
            col = j
print("{}\n{} {}".format(max, row + 1, col + 1))