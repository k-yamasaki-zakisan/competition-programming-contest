#https://atcoder.jp/contests/tokiomarine2020/tasks/tokiomarine2020_c

N, K = list(map(int, input().split()))
A = list(map(int, input().split()))

for _ in range(K):
    B = [0]*N
    for i in range(N):
        l = max(0,i-A[i])
        r = min(N-1, i+A[i])
        B[l] += 1
        if r+1 < N: B[r+1] -= 1
    for i in range(1,N):
        B[i] += B[i-1]
    B,A = A,B
    if min(A) == N:
        break
print(*A)
