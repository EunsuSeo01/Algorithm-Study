import sys

# 인덱스 번째의 수가 소수인지(1) 아닌지(0) 상태를 저장해두는 리스트 (최대 인풋 값이 123456)
is_prime_list = [0] + [1] * (2 * 123456 + 1)

# 에라토스테네스의 체를 활용
# 123456까지 다 돌면서 '소수의 배수'들을 다 0으로 미리 바꿔둔다.
for i in range(2, int(len(is_prime_list) ** 0.5)):
    if is_prime_list[i]:
        for j in range(i + i, len(is_prime_list), i):
            is_prime_list[j] = 0

# 0 나오기 전까지의 인풋 받기
input_list = []
while True:
    n = int(sys.stdin.readline().strip())
    if n == 0:
        break
    input_list.append(n)

# 위에서 미리 값을 업데이트 해둔 리스트에서 n + 1번째 인덱스부터 2 * n번째 인덱스의 값을 더하면 해당 범위에서 소수가 총 몇 개인지 알 수 있다!
for n in input_list:
    print(sum(is_prime_list[n + 1: 2 * n + 1]))
