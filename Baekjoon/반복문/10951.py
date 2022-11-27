import sys
while True :
    try :
        a,b = map(int, sys.stdin.readline().split())
        print(a + b)
    except :    # a,b 값을 입력하지 않고 엔터를 쳤을 때 while문이 종료되는 것!
        break
