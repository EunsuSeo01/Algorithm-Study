M, N = map(int, input().split(' '))
# 에라토스테네스의 체를 이용해서 소수의 배수들(합성수)을 제거할 것
# 소수 몇의 배수까지 확인해야 하는지 판단하기 위해 한계값을 구함
limit = int(N ** (1 / 2))
composite_set = set()

# 합성수의(소수가 아닌) 집합을 만들어주는 함수
def make_composite_set(num: int):
    # num을 제외한 num의 배수를 합성수 집합에 추가
    composite_set.update({t for t in range(num, N + 1, num) if t != num})

# 2부터 limit까지 돌면서 i를 제외한 i의 배수를 합성수 집합에 추가
for i in range(2, limit + 1):
    make_composite_set(i)

# M 이상 N 이하 중 소수를 출력
for i in range(M, N + 1):
    # 1은 소수에서 제외
    if i == 1:
        continue
    # 합성수 집합에 포함되지 않은 수들을 출력
    elif i not in composite_set:
        print(i)
