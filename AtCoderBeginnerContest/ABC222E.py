# https://atcoder.jp/contests/abc222/tasks/abc222_e

from collections import defaultdict
from collections import deque
from math import inf
MOD = 998244353


def bps(s: int, g: int):
    global W
    stack = deque([s])
    check = [inf]*N
    check[s] = 0
    while len(stack):
        now = stack.popleft()
        if now == g:
            break
        for next, i in root[now]:
            if check[now]+1 < check[next]:
                check[next] = check[now]+1
                stack.append(next)
    stack = deque([g])
    while len(stack):
        now = stack.popleft()
        for next, i in root[now]:
            if check[now]-1 == check[next]:
                W[i] += 1
                stack.append(next)


N, M, K = map(int, input().split())
A = list(map(int, input().split()))
UV = [list(map(int, input().split())) for _ in range(N-1)]
root = [[] for _ in range(N)]
for i, uv in enumerate(UV):
    u, v = uv
    u, v = u-1, v-1
    root[u].append((v, i))
    root[v].append((u, i))

W = [0] * (N - 1)
for i in range(M-1):
    s, g = A[i]-1, A[i+1]-1
    bps(s, g)

max_v = sum(W)
if max_v-K < 0 or (max_v-K) % 2:
    print(0)
    exit()
p = (max_v-K)//2
dp = [0]*(p+1)
dp[0] = 1
for v in W:
    for j in range(p, -1, -1):
        if j+v <= p:
            dp[j+v] += dp[j]
            dp[j+v] %= MOD
print(dp[-1])
