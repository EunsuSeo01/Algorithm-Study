n = int(input())
scores = list(map(int, input().split()))
M = max(scores)
new_avg = 0
for score in scores :
    score = score / M * 100
    new_avg += score
new_avg /= n
print(new_avg)
