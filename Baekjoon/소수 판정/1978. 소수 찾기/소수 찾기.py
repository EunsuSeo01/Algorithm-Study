N = int(input())
answer = 0
number = list(map(int, input().split(' ')))
for i in number:
    count = 0
    for j in range(1, i + 1):
        if i % j == 0:
            count += 1
    if count == 2:
        answer += 1
print(answer)