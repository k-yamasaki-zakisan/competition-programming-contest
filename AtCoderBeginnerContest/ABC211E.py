# https://atcoder.jp/contests/abc211/tasks/abc211_e

N = int(input())
K = int(input())
S = [list(input()) for _ in range(N)]
ans = set()
roots = set()


def dps(h, w, used):
    concated = ''
    for i in range(N):
        for j in range(N):
            concated += 'o' if used[i][j] else '-'
    if concated in roots:
        return

    if sum([sum(u) for u in used]) == K:
        ans.add(concated)
        return

    for h in range(N):
        for w in range(N):
            if not used[h][w] or S[h][w] == '#':
                continue
            for hh, ww in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
                nh, nw = h+hh, w+ww
                if 0 <= nh < N and 0 <= nw < N and S[nh][nw] == '.' and not used[nh][nw]:
                    used[nh][nw] = True
                    dps(nh, nw, used)
                    used[nh][nw] = False
    roots.add(concated)


for i in range(N):
    for j in range(N):
        if S[i][j] == '#':
            continue
        used = [[False] * N for _ in range(N)]
        used[i][j] = True
        dps(i, j, used)

print(len(ans))
