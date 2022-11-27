text = input()
alphabet_list = ["ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"]
sec = 0
for i in text:
    for j in alphabet_list:
        if j.__contains__(i):
            sec += alphabet_list.index(j) + 3
print(sec)
