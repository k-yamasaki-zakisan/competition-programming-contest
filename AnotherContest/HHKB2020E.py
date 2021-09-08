# https://atcoder.jp/contests/hhkb2020/tasks/hhkb2020_e

MOD = 10**9+7

H, W = map(int, input().split())
S = [input() for _ in range(H)]
free = 0
for s in S:
    free += s.count('.')

yoko = [[0]*W for _ in range(H)]
for h in range(H):
    tmp = 0
    for w in range(W):
        if S[h][w] == '#':
            tmp = 0
        else:
            tmp += 1
            yoko[h][w] = tmp
    for w in range(W-1, -1, -1):
        if yoko[h][w]:
            tmp = max(tmp, yoko[h][w])
            yoko[h][w] = tmp
        else:
            tmp = 0
take = [[0]*W for _ in range(H)]
for w in range(W):
    tmp = 0
    for h in range(H):
        if S[h][w] == '#':
            tmp = 0
        else:
            tmp += 1
            take[h][w] = tmp
    for h in range(H-1, -1, -1):
        if take[h][w]:
            tmp = max(tmp, take[h][w])
            take[h][w] = tmp
        else:
            tmp = 0
ans = 0
pow2 = [pow(2, 0, MOD)]
for i in range(free):
    pow2.append((pow2[-1]*2) % MOD)

for h in range(H):
    for w in range(W):
        if S[h][w] == '#':
            continue
        cnt = take[h][w]+yoko[h][w]-1
        ans += pow2[free-cnt]*(pow2[cnt]-1)
        ans %= MOD
print(ans)
