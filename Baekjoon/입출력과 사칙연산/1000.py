# 파이썬 입력은 input() 함수를 통해서 받는다.
# split() 함수를 이용해 a,b 각각에 입력값을 할당해준다.
# map() 함수를 이용해 input().split()으로 가져온 문자열 입력값을 int형으로 바꿔준다!
# Int 아니고 int인 것에 주의.

a,b = map(int, input().split())
print(a + b)
