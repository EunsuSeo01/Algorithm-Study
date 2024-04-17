# 최대공약수와 최소공배수 - 브론즈 1
a, b = map(int, input().split())

# 두 수의 곱을 mul에 저장
mul = a * b
gcd = 0
lcm = mul

# 최대공약수 구하기
while True:
    n = a % b
    # 나머지가 0이 되면 나누는 수가 gcd
    if n == 0:
        gcd = b
        break
    # 나눠지는 수와 나누는 수를 업데이트
    else:
        a = b
        b = n

# 최소공배수 구하기
# gcd가 1이면 처음 입력받은 두 값의 곱이 lcm이 된다
if gcd != 1:
    # 두 수의 곱은 최대공약수와 최소공배수의 곱과 같다
    lcm = int(mul / gcd)

print(f"{gcd}\n{lcm}")