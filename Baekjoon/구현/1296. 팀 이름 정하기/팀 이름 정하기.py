# 팀 이름 정하기 - 브론즈 1
import sys
yeondu = sys.stdin.readline().strip()
N = int(sys.stdin.readline().strip())
names = sorted([sys.stdin.readline().strip() for _ in range(N)])
max_percent = max_index = 0

for i in range(N):
    L = yeondu.count("L") + names[i].count("L")
    O = yeondu.count("O") + names[i].count("O")
    V = yeondu.count("V") + names[i].count("V")
    E = yeondu.count("E") + names[i].count("E")
    percent = ((L+O) * (L+V) * (L+E) * (O+V) * (O+E) * (V+E)) % 100
    if percent > max_percent:
        max_percent = percent
        max_index = i
print(names[max_index])