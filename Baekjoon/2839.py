N = int(input())
answer = []
a = 0
b = 0
c = 0
while True:
    b = (N - 3 * a) % 5
    c = (N - 3 * a) / 5
    if b == 0:
        answer.append(a + c)
    a += 1
    if c <= 0:
        break
if len(answer) == 0:
    print(-1)
else:
    print(int(min(answer)))

