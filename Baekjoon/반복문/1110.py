n = int(input())
i = 0
new_num = n

while True :
    temp = new_num // 10 + new_num % 10
    new_num = (new_num % 10) * 10 + temp % 10
    i += 1
    
    if n == new_num :
        print(i)
        break
