# https://atcoder.jp/contests/abc256/tasks/abc256_e

from heapq import heapify, heappop, heappush

N = int(input())
X = list(map(int, input().split()))
C = list(map(int, input().split()))
cost = [0] * N
for i in range(N):
    cost[X[i] - 1] += C[i]
cost_hp = [(costt, i) for i, costt in enumerate(cost)]
heapify(cost_hp)
seen = set()
ans = 0
while len(cost_hp):
    c, now = heappop(cost_hp)
    if now in seen:
        continue
    ans += c
    seen.add(now)
    cost[X[now] - 1] -= C[now]
    heappush(cost_hp, (cost[X[now] - 1], X[now] - 1))
print(ans)
