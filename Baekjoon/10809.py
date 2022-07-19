S = input()
alphabet = list("a b c d e f g h i j k l m n o p q r s t u v w x y z") # 문자열은 수정이 안 되기 때문에 list로 변환하여 수정한다!!

for i in range(0, len(alphabet), 2) : # 공백 부분은 지나가기 위해 인덱스 2칸씩 이동
    alphabet[i] = str(S.find(alphabet[i]))
    """ alphabet[i]가 S에서 처음 등장하는 인덱스를 찾는다
        없으면 -1이 들어간다
        -> 값이 int라서 str로 바꿔서 저장 """

print(''.join(alphabet))
