word = input()
cnt = 0
croatia_list = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
for croatia in croatia_list:
    if croatia in word:
        cnt += word.count(croatia)
        word = word.replace(croatia, ' ')  # 여기서 ''로 대체해버리면 남겨진 문자들로 새 크로아티아 문자를 이룰 수도 있기 때문에 공백으로 둔다.
word = word.replace(' ', '')  # 확인이 다 끝난 후 공백 부분을 제거한다.
cnt += len(word)
print(cnt)
