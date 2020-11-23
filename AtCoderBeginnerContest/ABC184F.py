from bisect import bisect_right
import itertools

N,T = map(int,input().split())
A = list(map(int,input().split()))

f_a = A[:N//2]
s_a = A[N//2:]

f_cnd = [0]
s_cnd = [0]
for i in range(1,len(f_a)+1):
    for v in itertools.combinations(f_a, i):
        f_cnd.append(sum(v))

for i in range(1,len(s_a)+1):
    for v in itertools.combinations(s_a, i):
        s_cnd.append(sum(v))
s_cnd.sort()

ans = 0
for f in f_cnd:
    tmp = T-f
    i = bisect_right(s_cnd, tmp)-1
    if 0 <= i:
        ans = max(ans,f+s_cnd[i])
print(ans)