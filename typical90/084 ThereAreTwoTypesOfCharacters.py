# https://atcoder.jp/contests/typical90/tasks/typical90_cf

from bisect import bisect_left

N = int(input())
S = list(input())
maru = []
batu = []
for i, s in enumerate(S):
    if s == 'o':
        maru.append(i)
    else:
        batu.append(i)
len_maru = len(maru)
len_batu = len(batu)
if len_maru == 0 or len_batu == 0:
    print(0)
    exit()

ans = 0
for i, s in enumerate(S):
    if s == 'o':
        index = bisect_left(batu, i)
        if index < len_batu:
            ans += N-batu[index]
    else:
        index = bisect_left(maru, i)
        if index < len_maru:
            ans += N-maru[index]
print(ans)
