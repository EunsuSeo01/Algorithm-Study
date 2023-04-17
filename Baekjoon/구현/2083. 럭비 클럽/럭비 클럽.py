# 럭비 클럽 - 브론즈 4
# 17세보다 많거나, 몸무게가 80kg 이상이면 성인부 그외에는 다 청소년부
import sys

while True:
    name, age, weight = sys.stdin.readline().strip().split()
    if name == "#" and age == "0" and weight == "0":
        break
    if int(age) > 17 or int(weight) >= 80:
        print(name, "Senior")
    else:
        print(name, "Junior")
