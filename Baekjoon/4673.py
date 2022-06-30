answer_set = set(range(1,10001))
generate_set = set()

# n과 n의 각 자리수를 더하는 함수
def d(n) :
    generate_num = n
    while n != 0 :
        generate_num += n % 10
        n = int(n / 10)
    return generate_num

for i in answer_set :
    generate_set.add(d(i))

answer_set = sorted(answer_set - generate_set)
for i in answer_set :
    print(i)
