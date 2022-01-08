# https://atcoder.jp/contests/arc130/tasks/arc130_b

H, W, C, Q = map(int, input().split())
TNC = [list(map(int, input().split())) for _ in range(Q)]
TNC_re = TNC[::-1]
tate = set()
yoko = set()
ans = [0]*C
for t, n, c in TNC_re:
    if t == 1:
        if n not in yoko:
            yoko.add(n)
            ans[c-1] += W-len(tate)
    else:
        if n not in tate:
            tate.add(n)
            ans[c-1] += H-len(yoko)
print(*ans)
