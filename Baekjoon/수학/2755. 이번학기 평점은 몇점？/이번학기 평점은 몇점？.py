# 이번 학기 평점은 몇 점? - 브론즈 1
import sys

grade_dict = {
    'A+': 4.3, 'A0': 4.0, 'A-': 3.7,
    'B+': 3.3, 'B0': 3.0, 'B-': 2.7,
    'C+': 2.3, 'C0': 2.0, 'C-': 1.7,
    'D+': 1.3, 'D0': 1.0, 'D-': 0.7,
    'F': 0.0
}

num = int(sys.stdin.readline().strip())
total_time = 0
answer = 0
for _ in range(num):
    _, time, grade = sys.stdin.readline().strip().split()
    time = int(time)
    answer += time * grade_dict.get(grade)
    total_time += time
    
# 평균 평점은 각 과목의 학점*성적을 모두 더한 뒤에, 총 학점으로 나누면 된다.
print(f"{round(answer / total_time + 10 ** (-len(str(answer / total_time)) - 1), 2):.2f}")
