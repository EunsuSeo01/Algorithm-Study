import sys
T = int(sys.stdin.readline().strip())

# 인덱스 번째의 수가 소수인지 아닌지 저장해두는 리스트 (최대 인풋 값이 10000)
prime_list = [i for i in range(0, 10001)]

# 에라토스테네스의 체를 활용
# 다 돌면서 '소수의 배수'들을 다 -1로 바꿔둔다.
for i in range(2, int(len(prime_list) ** 0.5)):
    if prime_list[i] != -1:
        for j in range(i + i, len(prime_list), i):
            prime_list[j] = -1

# 가능한 n의 골드바흐 파티션이 여러 가지인 경우에는 두 소수의 차이가 가장 작은 것을 출력한다는 조건이 있기 때문에
# n을 절반으로 나눠서 중간 지점에서부터 살펴보는 것이다.
def find_partition(n: int):
    half_n = n // 2
    while half_n >= 1:
        # 중간 지점의 숫자가 소수이고, (n - 중간지점의 숫자)를 한 값도 소수일 경우
        # 참고1: count 함수는 괄호 안의 값이 리스트에 없을 경우 0을 리턴한다.
        # 참고2: if 0은 거짓이다. 0이 아닌 수는 참으로 판단.
        if prime_list[half_n] != -1 and prime_list.count(n - half_n):
            # 해당 숫자 두개를 포맷팅하여 반환한다.
            return "{} {}".format(half_n, n - half_n)
        half_n -= 1

for _ in range(T):
    n = int(sys.stdin.readline().strip())
    # n의 골드바흐 파티션 찾기
    print(find_partition(n))