# 단어 정렬
import sys

N = int(sys.stdin.readline().strip())
# 입력을 N개를 받아서 집합으로 만든다 -> 중복된 단어 제거
words = set(sys.stdin.readline().strip() for i in range(N))
# 정렬 함수를 쓰기 위해 list로 형변환을 한다
words = list(words)
# words의 단어들을 사전 순으로 정렬한다
words.sort()
# 사전 순으로 정렬된 단어들을 길이 순으로 정렬한다 -> 같은 길이의 단어는 사전 순이 유지된다
words.sort(key=len)
for word in words:
    print(word)

