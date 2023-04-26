# 뒤집힌 덧셈 - 브론즈 1
X, Y = input().split()
X = X[::-1]
Y = Y[::-1]
total = int(X) + int(Y)
print(int(str(total)[::-1]))