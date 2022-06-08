i = int(input())
list = []

# 갯수만큼 입력 받아서 리스트에 저장
for i in range(i) :
    a,b = map(int, input().split())
    list.append(a)
    list.append(b)

# 리스트에서 값 2개씩 추출해서 합 계산
for index in range(0, len(list), 2) :
    print(list[index] + list[index + 1])
