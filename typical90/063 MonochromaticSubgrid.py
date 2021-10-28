# https://atcoder.jp/contests/typical90/tasks/typical90_bk

from itertools import combinations
from collections import defaultdict

H, W = map(int, input().split())
P = [list(map(int, input().split())) for _ in range(H)]
H_list = [i for i in range(H)]

ans = 0
for i in range(1, H+1):
    for h_list in combinations(H_list, i):
        memo = defaultdict(int)
        for w in range(W):
            tmp = set()
            for h in h_list:
                tmp.add(P[h][w])
            if len(tmp) == 1:
                memo[list(tmp)[0]] += 1
        if len(memo):
            ans = max(ans, max([val for val in memo.values()])*len(h_list))
print(ans)
