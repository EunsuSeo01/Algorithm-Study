N = int(input())
answer = []
three = 0
five = 0
while True:
    five = (N - 3 * three) / 5
    if (N - 3 * three) % 5 == 0:
        answer.append(int(three + five))
    if five <= 0:
        break
    else:
        three += 1
if len(answer) == 0:
    print(-1)
else:
    print(min(answer))