#https://atcoder.jp/contests/abc051/submissions/15294066

def warshall_floyd(d):
    #d[i][j]: iからjへの最短距離
    for k in range(n):
        for i in range(n):
            for j in range(n):
                d[i][j] = min(d[i][j],d[i][k] + d[k][j])
    return d
 
 
n,w = map(int,input().split()) #n:頂点数　w:辺の数
 
d = [[float("inf")]*n for i in range(n)]

E = [tuple(map(int, input().split())) for _ in range(w)]

#d[u][v] : 辺uvのコスト(存在しないときはinf)
for x,y,z in E:
    d[x-1][y-1] = z
    d[y-1][x-1] = z
for i in range(n):
    d[i][i] = 0 #自身のところに行くコストは０

root = warshall_floyd(d)

ans = 0

for x,y,z in E:
    if d[x-1][y-1] != z:
        ans += 1
print(ans)
