N = int(input())
answer = 0
# 띄어쓰기로 구분해서 input을 받고 int로 매핑한 값들을 list로 만든다.
number = list(map(int, input().split(' ')))
# list의 값들을 하나씩 순회
for i in number:
    count = 0
    # 1부터 i까지의 값들로 나눈 나머지가 0이 되는 경우를 센다.
    for j in range(1, i + 1):
        if i % j == 0:
            count += 1
    # 1과 i(자기자신)으로 나눈 나머지는 무조건 0이 되므로 count 값은 최소 2이다.
    # 2개인지 확인하고 맞으면 소수니까 answer + 1.
    if count == 2:
        answer += 1
print(answer)