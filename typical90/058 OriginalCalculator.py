# https://atcoder.jp/contests/typical90/tasks/typical90_bf

# ボタンを押して過去に同じ数字が出てないか探索
MOD = 10**5
N, K = map(int, input().split())
memo = [N]
memo_list = [0]*10**5
memo_list[N] = 1
while len(memo) <= K:
    tmp_num = memo[-1]
    next_add_num = sum([int(i) for i in list(str(tmp_num))])
    next_num = (tmp_num + next_add_num) % MOD
    if next_num == 0:
        print(0)
        exit()
    if 0 < memo_list[next_num]:
        first_num = next_num
        break
    memo.append(next_num)
    memo_list[next_num] = 1 + memo_list[tmp_num]

# ボタン上限回数ならばそのまま出力
if len(memo) == K+1:
    print(memo[-1])
# ループする周期を調べて該当のindexを計算して答えを出力
else:
    K -= (memo_list[first_num]-1)
    targe_cnt = memo_list[first_num]
    new_memo = [(i, num) for num, i in enumerate(memo_list) if targe_cnt <= i]
    new_memo = sorted(new_memo, key=lambda x: x[0])
    print(new_memo[K % len(new_memo)][1])
