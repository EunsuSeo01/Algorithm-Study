# 나머지와 몫이 같은 수 - 브론즈 1
import sys
N = int(sys.stdin.readline().strip())
answer = 0
num = 0

# num은 N-1까지만 가능
while num < N:
    # N * 몫 + 나머지 = 그 수
    # 에서 몫 == 나머지 == num일 때 
    # 그 수가 answer
    answer += N * num + num
    num += 1
    
print(answer)
