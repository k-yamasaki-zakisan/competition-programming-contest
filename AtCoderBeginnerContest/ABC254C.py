# https://atcoder.jp/contests/abc254/tasks/abc254_c

N, K = map(int, input().split())
A = list(map(int, input().split()))
l = [[] for _ in range(K)]
for i in range(N):
    l[i % K] += [A[i]]

for i in range(K):
    l[i].sort()

l2 = []
for i in range(N):
    l2 += [l[i % K][i // K]]
l3 = sorted(l2)

if l2 == l3:
    print("Yes")
else:
    print("No")
