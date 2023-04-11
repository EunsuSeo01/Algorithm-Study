# 직사각형에서 탈출 - 브론즈 3
input = list(map(int, input().split()))
input[2] = input[2] - input[0]
input[3] = input[3] - input[1]

# 4개의 값 중 최소값을 찾는다
answer = sorted(input)
print(answer[0])