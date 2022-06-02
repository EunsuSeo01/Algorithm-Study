# 함수
def hello() :
    print("안녕하세요 여러분 파이썬 공부합시다")

hello()

# 파라미터 있으면 그냥 () 안에 넣어주면 됨.
def function(param) :
    print(param)

function(122 + 123)

# 리턴값 있는 함수.
def returnFive() :
    return 5    # 함수가 호출된 자리에 가죽을 남기는 것.

returnFive()

print(returnFive())     # print(5)

# 파라미터 있고 리턴값 있는 함수.
def function2(a, b) :
    c = a + b
    return c

print(function2(3, 3))