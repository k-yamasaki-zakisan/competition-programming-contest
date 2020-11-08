# https://atcoder.jp/contests/abc182/tasks/abc182_d

N = int(input())
A = list(map(int,input().split()))
AA = [0]*N
AAA = 0
for i in range(N):
    AA[i] = AA[i-1]+AAA+A[i]
    AAA = AAA+A[i]

max_v = max(AA)
i_b = AA.index(max_v)
ans = max(max_v,0)
tmp = AA[i_b-1]
for i in range(i_b):
    tmp += A[i]
    ans = max(tmp,ans)
if i_b < N-1:
    tmp = AA[i_b]
    for i in range(i_b+1):
        tmp += A[i]
        ans = max(tmp,ans)
print(ans)