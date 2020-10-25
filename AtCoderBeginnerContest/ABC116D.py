# https://atcoder.jp/contests/abc116/tasks/abc116_d

N,K = map(int,input().split())
TD = [list(map(int,input().split())) for _ in range(N)]
TD = sorted(TD, key=lambda x: -x[1])
ex_pop = []
kind = 0
prim_k = {}
ans = 0
for i in range(K):
    t,d = TD[i]
    ans += d
    if t in prim_k:
        ex_pop.append(d)
    else:
        prim_k[t] = d
        kind += 1
# ボーナスポイント追加
ans += kind**2

tmp = ans
for i in range(K,N):
    t,d = TD[i]
    # 種類が増えたときの場合を全てみてみてansと比べて最大値をとってくる
    if t not in prim_k and len(ex_pop):
        prim_k[t] = d
        tmp = tmp-ex_pop.pop()+d-kind**2+(kind+1)**2
        kind += 1
        ans = max(ans,tmp)
print(ans)