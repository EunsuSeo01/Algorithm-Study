numbers = input().split()
number_list = []
for i in numbers :
    number_list.append(int("".join(reversed(i))))
print(max(number_list))