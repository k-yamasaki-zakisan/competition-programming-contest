# https://atcoder.jp/contests/past202005-open/tasks/past202005_j

from bisect import bisect_left
N,M = map(int,input().split())
A = list(map(int,input().split()))
ans = [-1]*N
for i in range(M):
    index = bisect_left(ans, A[i])
    if index == 0:
        print(-1)
    else:
        ans[index-1] = A[i]
        print(N-index+1)