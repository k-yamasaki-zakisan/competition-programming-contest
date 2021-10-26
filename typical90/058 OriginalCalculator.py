# https://atcoder.jp/contests/typical90/tasks/typical90_bf

MOD = 10**5

N, K = map(int, input().split())
memo = set()
memo.add(N)
o_num = [N]
in_flag = True
for _ in range(K):
    num = o_num[-1]
    num += sum(map(int, list(str(num))))
    num %= MOD
    if num not in memo:
        o_num.append(num)
        memo.add(num)
    else:
        last_num = num
        in_flag = False
        break
if in_flag:
    print(o_num[-1])
    exit()
f = o_num.index(last_num)
K -= f
ans_i = K % (len(o_num)-f)+f
print(o_num[ans_i])
