N = int(input())
answer = []
three = 0
five = 0
while True:
    three = (N - 5 * five) / 3
    if three < 0:
        break
    if (N - 5 * five) % 3 == 0:
        answer.append(three + five)
    five += 1
if len(answer) == 0:
    print(-1)
else:
    print(int(min(answer)))