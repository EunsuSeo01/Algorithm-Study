hour, minute = map(int, input().split())
interval = 45

if minute >= interval :
    minute -= interval
else :
    minute = (60 - (interval - minute))
    if hour >= 1 :
        hour -= 1
    else :
        hour = 23

print(hour, minute)
