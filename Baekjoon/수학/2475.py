# 검증수 - 브론즈 5
nums = list(map(int, input().split()))
sum = 0

# 각 요소를 제곱한 값을 합한다
for n in nums:
    sum += n**2

# 합을 10으로 나눈 나머지를 게산
print(sum % 10)