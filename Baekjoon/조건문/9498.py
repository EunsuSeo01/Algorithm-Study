# 파이썬은 두 개 이상의 조건을 한번에 점검할 때 and, or, not 논리 연산자를 사용할 수 있다.
# 파이썬에서는 아래의 코드처럼 범위를 비교할 때 변수를 가운데에 두고 양쪽에 범위를 적는 문법도 허용한다.

score = int(input())
if 90 <= score <= 100 :
    print("A")
elif 80 <= score < 90 :
    print("B")
elif 70 <= score < 80 :
    print("C")
elif 60 <= score < 70 :
    print("D")
else :
    print("F")
