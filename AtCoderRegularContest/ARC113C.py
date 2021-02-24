# https://atcoder.jp/contests/arc113/tasks/arc113_c

from collections import Counter

S = input().strip()
ans = 0
cnt = 0
c_old = "_"
counter = Counter()
for c in S[::-1]:
    if c == c_old:
        ans += cnt - counter[c]
        counter = Counter()
        counter[c] += cnt
    counter[c] += 1
    c_old = c
    cnt += 1

print(ans)
