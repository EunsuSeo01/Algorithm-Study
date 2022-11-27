X = int(input())
num_left = 0
num_right = 1
count = 1
while True:
    if num_left < X <= num_right:
        break
    else:
        count += 1
        num_left = num_right
        num_right += count
if count % 2 == 0:
    print("{}/{}".format(X - num_left, num_right + 1 - X))
else:
    print("{}/{}".format(num_right + 1 - X, X - num_left))
