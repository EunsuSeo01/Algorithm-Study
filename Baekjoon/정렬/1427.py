# 1427: 소트인사이드
N = input()
st = ""
# 입력 받은 수의 각 자리 숫자를 원소로 가지는 리스트를 생성 -> 정렬을 위해
li = [i for i in N]
# 리스트 내림차순 정렬
li.sort(reverse=True)
# 내림차순 정렬이 된 리스트의 각 원소를 +를 통해 '하나의 문자열'로 이어붙인다
for j in li:
    st += str(j)
print(st)
