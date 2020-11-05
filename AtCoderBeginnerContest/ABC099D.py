# https://atcoder.jp/contests/abc099/tasks/abc099_d

N,M = map(int,input().split())
D = [list(map(int,input().split())) for _ in range(M)]
C = [list(map(int,input().split())) for _ in range(N)]

# 同色グループを作成
colors = [[] for _ in range(3)]
for i in range(N):
    for j in range(N):
        k = (i+1+j+1)%3
        colors[k].append(C[i][j])

# 色変するグループ毎にどの色に変わるとコストがどれだけかかるかをメモ
d = [[0]*M for _ in range(3)]
for i in range(M):
    for j in range(3):
        for k in range(len(colors[j])):
            d[j][i] += D[colors[j][k]-1][i]

# 色変するのに最もコストが低い組み合わせを全探索
ans = 10**10
for i in range(M):
    for j in range(M):
        for k in range(M):
            if (i-j)*(j-k)*(k-i) == 0:
                continue
            tmp = d[0][i]+d[1][j]+d[2][k]
            ans = min(ans, tmp)
print(ans)