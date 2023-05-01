N = int(input())

if N == 1:
    print(666)
elif N == 2:
    print(1666)
elif N == 3:
    print(2666)
elif N == 4:
    print(3666)
elif N == 5:
    print(4666)
elif N == 6:
    print(5666)
else:
    num = 5666
    turn = 6
    while True:
        num += 1
        if str(num).count("666") >= 1:
            turn += 1
            if turn == N:
                print(num)
                break