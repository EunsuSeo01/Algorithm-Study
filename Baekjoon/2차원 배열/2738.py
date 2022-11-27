import sys

N, M = map(int, sys.stdin.readline().strip().split(' '))
one = []
two = []

# append를 이용해서 값을 추가하기 때문에 위에서 그냥 빈 list로 선언해 두어도 문제가 없다. 인덱스에 직접 접근해서 값을 넣는 게 아니니까.
# append를 이용해서 1차원 배열의 한 인덱스에 1차원 배열을 넣는다. -> 2차원 배열의 형태가 된다!!!
for i in range(N):
    # map 형태를 그대로 append 하면 안 된다. print 하면 map 객체가 그대로 나옴.
    # map을 통해 한 줄에 적힌 숫자 여러 개가 다 int로 변환돼서 반환되기 때문에 이것을 그냥 list화 해서 append 하면 된다!
    one.append(list(map(int, sys.stdin.readline().strip().split(' '))))

for j in range(N):
    two.append(list(map(int, sys.stdin.readline().strip().split(' '))))

for i in range(N):
    for j in range(M):
        print(one[i][j] + two[i][j], end=' ')
    print()
