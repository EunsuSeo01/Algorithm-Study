# DNA 해독 - 브론즈 1
import sys

dna_table = [
    ['A', 'C', 'A', 'G'],
    ['C', 'G', 'T', 'A'],
    ['A', 'T', 'C', 'G'],
    ['G', 'A', 'G', 'T']
]
dna_dict = {
    'A': 0,
    'G': 1,
    'C': 2,
    'T': 3
}
N = int(sys.stdin.readline().strip())
dna_input = sys.stdin.readline().strip()
dna_input = list(dna_input)

while N > 1:
    # 마지막 값 2개 pop
    last_index = dna_dict[dna_input.pop()]
    sec_last_index = dna_dict[dna_input.pop()]
    # 염기서열 표에서 뽑아와서 맨 끝에 append
    dna_input.append(dna_table[sec_last_index][last_index])
    N -= 1
print(dna_input[0])
