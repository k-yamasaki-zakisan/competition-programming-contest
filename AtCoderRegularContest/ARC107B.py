# https://atcoder.jp/contests/arc107/tasks/arc107_b

N,K = map(int,input().split())
ans = 0
for i in range(2,2*N+1):
    j = i-K
    if 2 <= j <= 2*N:
        ans += (min(i-1, N*2+1-i))*(min(j-1, N*2+1-j))
print(ans)