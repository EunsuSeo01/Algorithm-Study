# 삼각형 외우기 - 브론즈 4
import sys
n1 = int(sys.stdin.readline().strip())
n2 = int(sys.stdin.readline().strip())
n3 = int(sys.stdin.readline().strip())

if n1 == 60 and n2 == 60 and n3 == 60:
    print("Equilateral")
elif n1 + n2 + n3 == 180:
    if n1 == n2 or n2 == n3 or n1 == n3:
        print("Isosceles")
    else:
        print("Scalene")
else:
    print("Error")