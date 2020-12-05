# https://atcoder.jp/contests/abc022/tasks/abc022_c

INF = float('inf')

def warshall_floyd(d):
    for k in range(N):
        for i in range(N):
            for j in range(N):
                d[i][j] = min(d[i][j],d[i][k] + d[k][j])
    return d

N,M = map(int,input().split())
UVL = [list(map(int,input().split())) for _ in range(M)]
cost = [[INF]*N for i in range(N)] 
first_step = []
for u,v,l in UVL:
    u, v = u-1, v-1
    if u == 0 or v == 0:
        first_step.append([u, v, l])
    else:
        cost[u][v] = l
        cost[v][u] = l
for i in range(N):
    cost[i][i] = 0

result = warshall_floyd(cost)

ans = INF
for i, fufvfl in enumerate(first_step):
    fu, fv, fl = fufvfl
    start = max(fu,fv)
    for j, uvl in enumerate(first_step):
        if i == j:
            continue
        eu, ev, el = uvl
        end = max(eu,ev)
        ans = min(ans, result[start][end]+fl+el)
if ans == INF:
    print(-1)
else:
    print(ans)