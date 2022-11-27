M = int(input())
N = int(input())

prime_list = []

# list의 값들을 하나씩 순회
for i in range(M, N + 1):
    isPrime = True
    # 2부터 i-1까지의 값들로 나눈 나머지가 0이 되는 경우를 센다.
    for j in range(2, i + 1):
        # 이 경우에 걸리면 i가 될 때까지 루프를 다 돌았으면서도 isPrime이 참인 거니까 j는 소수. j를 prime_list에 추가.
        if j == i and isPrime:
            prime_list.append(j)
        # 이 경우가 있다는 것은 1과 자기 자신 외에 나누어떨어지는 수가 있다는 것이므로 소수가 아닌 것이다.
        elif i % j == 0:
            isPrime = False
            break
if len(prime_list) == 0:
    print(-1)
else:
    print(sum(prime_list), prime_list[0])
    