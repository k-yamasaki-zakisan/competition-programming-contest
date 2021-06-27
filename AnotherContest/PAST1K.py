# https://atcoder.jp/contests/past201912-open/tasks/past201912_k
# 備考：pythonでないと通らない(pypyダメ)

import sys
sys.setrecursionlimit(10**7)

N = int(input())
P = [int(input()) for _ in range(N)]
Q = int(input())
AB = [list(map(int, input().split())) for _ in range(Q)]
sv_tree = [[] for _ in range(N)]
President = -1
for i, p in enumerate(P):
    if p == -1:
        President = i
    else:
        sv_tree[i].append(p-1)
        sv_tree[p-1].append(i)
queries = [[] for _ in range(N)]
for i, ab in enumerate(AB):
    a, b = ab
    queries[a-1].append((b-1, i))


def dps(vNow, vEx):
    for b, i in queries[vNow]:
        anss[i] = b in setAnc
    setAnc.add(vNow)
    for vNext in sv_tree[vNow]:
        if vNext == vEx:
            continue
        dps(vNext, vNow)
    setAnc.remove(vNow)


anss = [False]*Q
setAnc = set()
dps(President, -1)
for ans in anss:
    print('Yes' if ans else 'No')
