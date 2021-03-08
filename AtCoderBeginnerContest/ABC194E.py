# https://atcoder.jp/contests/abc194/tasks/abc194_e

N, M = map(int, input().split())
A = list(map(int, input().split()))

max_a = max(A)+5
memo = [0]*max_a
for i in range(M):
    a = A[i]
    memo[a] += 1

for i, me in enumerate(memo):
    if me == 0:
        ans = i
        break

for i in range(M, N):
    a = A[i]
    b = A[i-M]
    memo[a] += 1
    memo[b] -= 1
    if memo[b] == 0 and b < ans:
        ans = b
print(ans)
