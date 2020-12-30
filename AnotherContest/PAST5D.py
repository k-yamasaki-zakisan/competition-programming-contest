# https://atcoder.jp/contests/past202012-open/tasks/past202012_d

from collections import defaultdict
N = int(input())
S = [input() for _ in range(N)]

memo = defaultdict(list)
for s in S:
    memo[int(s)].append(s)

memo = sorted(memo.items(), key=lambda x: x[0])
for val in memo:
    val = val[1]
    val.sort(key=len, reverse=True)
    for v in val:
        print(v)
