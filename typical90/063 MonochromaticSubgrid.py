# https://atcoder.jp/contests/typical90/tasks/typical90_bk

from collections import defaultdict

H, W = map(int, input().split())
P = [list(map(int, input().split())) for _ in range(H)]
ans = 0
# １行の同じ文字の最大数をカウント
for h in range(H):
    tmp = defaultdict(int)
    for w in range(W):
        tmp[P[h][w]] += 1
    ans = max(ans, max([val for val in tmp.values()]))

# 2行以上の同じ文字の最大数をカウント
for i in range(2 ** H):
    h_list = []
    for j in range(H):
        if ((i >> j) & 1):
            h_list.append(j)
    if not len(h_list) or len(h_list) == 1:
        continue

    tmp_cnt = defaultdict(int)
    for w in range(W):
        tmp = set()
        for h in h_list:
            tmp.add(P[h][w])
        if len(tmp) == 1:
            tmp_cnt[list(tmp)[0]] += 1
    if len(tmp_cnt):
        ans = max(ans, len(h_list)*max([val for val in tmp_cnt.values()]))
print(ans)
