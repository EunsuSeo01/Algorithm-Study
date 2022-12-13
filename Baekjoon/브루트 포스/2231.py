N = int(input())
now = 0
total = 0
M = 0
# 1부터 N - 1까지 보면서 찾기
for i in range(1, N):
    # 현재 보고 있는 수를 저장하는 변수 now
    now = i
    # total에 (현재 수 + 현재 수의 각 자리수의 합)을 저장
    total = now
    # 나머지가 0이 될 때까지 반복
    while i % 10 != 0:
        # 각 자리의 숫자를 구해서 더한다
        total += i % 10
        i = i // 10
    # total의 값이 N과 같으면 now는 N의 생성자이다
    if N == total:
        M = now
        # 가장 작은 생성자를 구했으니 break로 for문 탈출
        break
print(M)
