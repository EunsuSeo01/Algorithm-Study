# 미국 스타일 - 브론즈 3
import sys
T = int(sys.stdin.readline().strip())
lb_unit = 2.2046
l_unit = 3.7854
kg_unit = 0.4536
g_unit = 0.2642
for _ in range(T):
    value, unit = sys.stdin.readline().strip().split()
    value = float(value)
    if unit == 'kg':
        value *= lb_unit
        unit = 'lb'
    elif unit == 'l':
        value *= g_unit
        unit = 'g'
    elif unit == 'lb':
        value *= kg_unit
        unit = 'kg'
    else:
        value *= l_unit
        unit = 'l'
    print("{:.4f}".format(value), unit)
