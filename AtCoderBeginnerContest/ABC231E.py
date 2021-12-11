# https://atcoder.jp/contests/abc231/tasks/abc231_e

N, X = map(int, input().split())
A = list(map(int, input().split()))
A = A[::-1]
L = [0]*N
n = X
for i in range(N):
    L[i] = n//A[i]
    n %= A[i]
DP = [[0]*2 for _ in range(N)]
DP[0][0] = L[0]
DP[0][1] = L[0]+1
for i in range(N-1):
    DP[i+1][0] = min(DP[i][0]+L[i+1], DP[i][1]+A[i]//A[i+1]-L[i+1])
    DP[i+1][1] = min(DP[i][0]+L[i+1]+1, DP[i][1]+A[i]//A[i+1]-L[i+1]-1)
print(DP[-1][0])
