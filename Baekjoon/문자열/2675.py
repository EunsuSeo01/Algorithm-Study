T = int(input())
for i in range(0, T) :
    P = "" # initialize
    R, S = input().split()
    R = int(R)
    for j in S :
        P += j*R # string 연산! 문자 j를 R번 반복한 문자열을 P에 이어붙이기
    print(P)
