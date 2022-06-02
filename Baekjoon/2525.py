hour, minute = map(int, input().split())
cooking_time = int(input())

if minute + cooking_time >= 60 :
    added_hour = int((minute + cooking_time) / 60)
    hour += added_hour
    if hour >= 24 :
        hour -= 24
    minute = (minute + cooking_time) % 60
else :
    minute += cooking_time

print(hour, minute)
