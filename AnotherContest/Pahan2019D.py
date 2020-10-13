N = int(input())
source_m = [list(input()) for _ in range(5)]
source_t = [[] for _ in range(N)]
for i in range(N):
    for j in range(5):
        source_t[i].append(source_m[j][i])

color_memo = []
for i in range(N):
    w = 0
    b = 0
    r = 0
    for j in range(5):
        if source_t[i][j] == 'W':
            w += 1
        elif source_t[i][j] == 'B':
            b += 1
        elif source_t[i][j] == 'R':
            r += 1
    color_memo.append([w,b,r])

#DBでズレ前の行とズレながら最低値を管理
dp = [[10000000000000]*3 for _ in range(N+1)]
dp[0][0] = dp[0][1] = dp[0][2] = 0
for i in range(N):
    for j in range(3):
        for k in range(3):
            if j == k:
                continue
            dp[i+1][j] = min(dp[i+1][j], dp[i][k]+5-color_memo[i][j])

print(min(dp[-1]))