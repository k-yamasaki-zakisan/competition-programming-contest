# https://atcoder.jp/contests/past201912-open/tasks/past201912_j

from heapq import heappop, heappush, heapify


def dij(cost: list, start: int) -> list:
    d = [INF] * (H*W)
    d[start] = 0

    q = [(d[start], start)]
    heapify(q)
    while q:
        du, u = heappop(q)
        if d[u] < du:
            continue
        for v, weight in cost[u]:
            if du + weight < d[v]:
                d[v] = du + weight
                heappush(q, (d[v], v))
    return d


INF = float('inf')
H, W = map(int, input().split())
root = [list(map(int, input().split())) for _ in range(H)]
cost = [[] for _ in range(H*W)]
# コストテーブルの作成
for h in range(H):
    for w in range(W):
        for y, x in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
            nh, nw = h+y, w+x
            if 0 <= nh < H and 0 <= nw < W:
                cost[W*h+w].append((W*nh+nw, root[nh][nw]))

# スタート、中間地点、ゴールからのそれぞれのポイントのコスト算出
to_start = dij(cost, (H-1)*W)
to_mid = dij(cost, H*W-1)
to_end = dij(cost, W-1)

ans = INF
for i in range(W*H):
    if i in (W-1, (H-1)*W):
        continue
    h, w = i//W, i % W
    tmp_sum_cost = to_start[i]+to_mid[i]+to_end[i]-2*root[h][w]
    ans = min(ans, tmp_sum_cost)
print(ans)
