# 모음의 개수 - 브론즈 4
import sys

sentence = ""
data = ['a', 'e', 'i', 'o', 'u']

# '#'자가 오면 종료
while True:
    cnt = 0
    # 입력을 다 소문자로 변환해서 저장
    sentence = sys.stdin.readline().strip().lower()
    if sentence == "#":
        break
    for d in data:
        # 문장에 모음의 개수를 세서 합친다
        cnt += sentence.count(d)
    print(cnt)