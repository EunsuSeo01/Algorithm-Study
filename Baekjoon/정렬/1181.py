# 단어 정렬
import sys

N = int(sys.stdin.readline().strip())
words = set([sys.stdin.readline().strip() for i in range(N)])
lengths = [[len(word), word] for word in words]
lengths.sort()
for _, w in lengths:
    print(w)
