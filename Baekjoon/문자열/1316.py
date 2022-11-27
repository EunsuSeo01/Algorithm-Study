N = int(input())
answer = 0
for _ in range(N):
    index = 0
    alphabet_list = []
    location = 0
    word = input()
    for i in word:
        if i in alphabet_list:
            if i != alphabet_list[index - 1]:
                break
        else:
            alphabet_list.append(i)
            index += 1
        location += 1
    if location == len(word):
        answer += 1

print(answer)