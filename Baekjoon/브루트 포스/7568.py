# 덩치 - 실버 5
import sys

N = int(sys.stdin.readline().strip())
two_list = []
answer = []
for _ in range(N):
    xy_list = list(map(int, sys.stdin.readline().strip().split()))
    two_list.append(xy_list)
    answer.append(1)  # 등수를 1로 초기화

# 브루트 포스
# 하나씩 다 체크해본다
for i in range(N):
    for j in range(N):
        if i != j:
            # i가 j보다 덩치가 더 크다
            if two_list[i][0] > two_list[j][0] and two_list[i][1] > two_list[j][1]:
                # answer의 j 자리에 +1 => j보다 덩치 큰 사람의 개수를 카운팅
                answer[j] += 1
print(*answer)  # *를 사용하면 리스트 압축 해제를 할 수 있다! 요소들이 대괄호 없이 한번에 출력된다.
