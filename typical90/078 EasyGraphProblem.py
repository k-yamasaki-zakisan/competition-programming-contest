# https://atcoder.jp/contests/typical90/tasks/typical90_bz

N, M = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(M)]
ROOT = [[] for _ in range(N)]
for a, b in AB:
    a, b = a-1, b-1
    ROOT[a].append(b)
    ROOT[b].append(a)

ans = 0
for n in range(N):
    tmp = 0
    for r in ROOT[n]:
        if r < n:
            tmp += 1
    if tmp == 1:
        ans += 1
print(ans)
