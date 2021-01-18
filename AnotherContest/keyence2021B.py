# https://atcoder.jp/contests/keyence2021/tasks/keyence2021_b

from collections import Counter

N, K = map(int, input().split())
A = list(map(int, input().split()))
A_cnt = Counter(A)
ans = 0
servive_box = K
for i in range(300001):
    if i in A_cnt:
        val = A_cnt[i]
        if val < servive_box:
            ans += (servive_box-val)*i
            servive_box = val
    else:
        ans += servive_box*i
        break
print(ans)
