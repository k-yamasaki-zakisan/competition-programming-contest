# https://atcoder.jp/contests/arc120/tasks/arc120_a

N = int(input())
A = list(map(int, input().split()))
s = [0]*(N+1)
for i in range(1, N+1):
    s[i] = s[i-1]+A[i-1]
maxs = 0
sum = 0
answer = 0
for j in range(N):
    sum += s[j+1]
    maxs = max(maxs, A[j])
    print(sum+maxs*(j+1))
