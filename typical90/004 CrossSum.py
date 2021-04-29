# https://atcoder.jp/contests/typical90/tasks/typical90_d

H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]
a_tate = []
a_yoko = []
for a in A:
    a_yoko.append(sum(a))
for w in range(W):
    tmp = 0
    for h in range(H):
        tmp += A[h][w]
    a_tate.append(tmp)
ans = [[] for _ in range(H)]
for h in range(H):
    for w in range(W):
        tmp = a_yoko[h]+a_tate[w]-A[h][w]
        ans[h].append(tmp)

for a in ans:
    print(*a)
