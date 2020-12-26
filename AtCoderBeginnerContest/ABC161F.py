# https://atcoder.jp/contests/abc161/tasks/abc161_f

def prime(p):
    memo = set()
    for i in range(1, (int(p**0.5)+1)):
        if p % i == 0:
            if i != 1:
                memo.add(i)
            memo.add(p//i)
    return memo


N = int(input())
# 2は例外で処理する
if N == 2:
    print(1)
    exit()
# 割り算しない場合
ans = prime(N-1)
cnd_ans = prime(N)
for i in cnd_ans:
    copy_n = N
    while copy_n % i == 0:
        copy_n //= i
    if copy_n % i == 1:
        ans.add(i)

print(len(ans))
