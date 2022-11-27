text = input()
count = 0
count = text.count(" ") # 전체 공백 개수
last_index = len(text)-1
if text[0] == " " and text[last_index] == " ":
    count -= 1
elif text[0] != " " and text[last_index] != " ":
    count += 1
print(count)