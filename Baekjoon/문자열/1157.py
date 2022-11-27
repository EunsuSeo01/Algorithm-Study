text = input().upper()
dic = {}
for i in text :
    if dic.get(i) == None :
        dic[i] = 1
    else :
        dic[i] += 1
max_list = [k for k,v in dic.items() if max(dic.values()) == v]
if len(max_list) == 1 :
    print(max_list[0])
else :
    print("?")
