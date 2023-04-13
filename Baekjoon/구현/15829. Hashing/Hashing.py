# Hashing - 브론즈 2
r = 31
mod = 1234567891
alphabets = "abcdefghijklmnopqrstuvwxyz"

L = int(input())
eng = input()

sum = 0
num = 0
for i in range(0, L):
    # eng 값들 하나씩 순회하며 해당 알파벳이 a~z 중 몇 번째 알파벳인지
    index = alphabets.index(eng[i]) + 1
    # 공식에 따라 합계 구하기
    sum += index * r ** num
    # 갈수록 증가하는 거듭제곱 num
    num += 1

# 합계를 mod 값으로 나눈 것의 나머지를 출력
print(sum % mod)