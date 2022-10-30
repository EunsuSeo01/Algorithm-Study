n = int(input())
sequence = 1
plus = 1
while True:
    if n <= plus:
        break
    else:
        plus += sequence * 6
        sequence += 1
print(sequence)
