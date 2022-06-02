first_num = int(input())
second_num = input()

hundreds = int(second_num[0])
tens = int(second_num[1])
units = int(second_num[2])

print(first_num * units)
print(first_num * tens)
print(first_num * hundreds)
print(first_num * units + first_num * tens * 10 + first_num * hundreds * 100)
