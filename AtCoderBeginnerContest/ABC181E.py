# https://atcoder.jp/contests/abc181/tasks/abc181_e
# 身長差の累積和を２種類作成して先生の変身身長が生徒のどこに入るのか二分探索

import bisect
N,M = map(int,input().split())
H = list(map(int,input().split()))
W = list(map(int,input().split()))
H.sort()
ans = 10**10

if N == 1:
    for w in W:
        ans = min(ans,abs(w-H[0]))
    print(ans)
    exit()

gu = [0]*(N//2)
ki = [0]*(N//2)
for i in range(0,N-1,2):
    sa = H[i+1]-H[i]
    gu[i//2] = gu[i//2-1]+sa
for i in range(1,N,2):
    sa = H[i+1]-H[i]
    ki[i//2] = ki[i//2-1]+sa

for i,val in enumerate(W):
    in_i = bisect.bisect_left(H,val)
    if in_i == 0 or in_i == 1:
        tmp = abs(val-H[0])+ki[-1]
    elif in_i == N or in_i == N-1:
        tmp = abs(val-H[-1])+gu[-1]
    else:
        h_i = in_i-in_i%2
        n_sa = abs(val-H[h_i])
        tmp = gu[h_i//2-1]+ki[-1]-ki[h_i//2-1]+n_sa
    ans = min(ans, tmp)
print(ans)