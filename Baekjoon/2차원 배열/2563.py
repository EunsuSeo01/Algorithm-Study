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
            # 애초부터 점의 위치를 tuple의 형태로 list에 넣는다.
            # -> tuple은 immutable하기 때문에 tuple로 구성된 list는 set 함수의 인자가 될 수 있다.
            dots.append((x + i, y + j))

# 중복되는 점들만 제거하고 점의 개수를 세면 그것이 검은 영역의 넓이가 된다.
# set을 통해 집합으로 변환하여 중복을 없애고 남은 점들의 개수를 센다. -> 답
print(len(set(dots)))
