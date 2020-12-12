# https://atcoder.jp/contests/abc078/tasks/arc085_b

N,Z,W = map(int,input().split())
A = list(map(int,input().split()))
if 1 < N:
    ans = max(abs(A[-2]-A[-1]), abs(W-A[-1]))
else:
    ans = abs(W-A[-1])
print(ans)