# https://atcoder.jp/contests/abc186/tasks/abc186_d

N = int(input())
A = list(map(int, input().split()))
A.sort(reverse=True)
ruiseki_A = [0]*N
ruiseki_A[0] = A[0]
for i in range(1, N):
    ruiseki_A[i] = ruiseki_A[i-1]+A[i]
ans = 0
for i in range(N):
    ans += A[i]*(N-i-1)-(ruiseki_A[-1]-ruiseki_A[i])
print(ans)
