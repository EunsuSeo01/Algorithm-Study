# 2563번: 색종이
import sys
n = int(sys.stdin.readline())
dots = []

# 입력값 받기
for _ in range(n):
    x, y = map(int, sys.stdin.readline().split(' '))
    # 검은색 색종이가 차지하는 모든 점들의 위치를 좌표화(x,y)하여 리스트로 저장한다.
    # -> 2차원 배열 형태를 띄게 됨.
    for i in range(1, 11):
        for j in range(1, 11):
            dots.append([x + i, y + j])

# 중복되는 점들만 제거하고 점의 개수를 세면 그것이 검은 영역의 넓이가 된다.
# 중복되는 점을 제거하기 위해 set() 함수를 사용할 것인데, 2차원 list는 set 함수의 파라미터로 들어갈 수 없다.
# 그렇기 때문에 2차원 list의 각 원소를 'immutable한 tuple의 형태'로 바꾸는 과정을 거쳐야 한다.
dots_tuple = [tuple(i) for i in dots]  # [(1,2), (3,4), ...]

# set을 통해 집합으로 변환하여 중복을 없애고 남은 점들의 개수를 센다. -> 답
print(len(set(dots_tuple)))
