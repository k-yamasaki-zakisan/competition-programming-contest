# https://atcoder.jp/contests/typical90/tasks/typical90_aj

INF = float('inf')
N, Q = map(int, input().split())
XY = [list(map(int, input().split())) for _ in range(N)]
Queries = [int(input()) for _ in range(Q)]
plus_max, plus_min = -INF, INF
minus_max, minus_min = -INF, INF
# ２次元グラフの4隅の頂点で原点から最も遠い点を記録
for x, y in XY:
    plus_max = max(plus_max, x+y)
    plus_min = min(plus_min, x+y)
    minus_max = max(minus_max, x-y)
    minus_min = min(minus_min, x-y)

# 四隅の点から最も遠い距離を算出
for q in Queries:
    q -= 1
    xt, yt = XY[q]
    plus_tmp = max(abs(plus_max-(xt+yt)), abs(plus_min-(xt+yt)))
    minus_tmp = max(abs(minus_max-(xt-yt)), abs(minus_min-(xt-yt)))
    print(max(plus_tmp, minus_tmp))
