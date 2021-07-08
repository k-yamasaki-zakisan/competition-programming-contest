# https://atcoder.jp/contests/typical90/tasks/typical90_ci

def warshall_floyd(d):
    for k in range(N):
        for i in range(N):
            for j in range(N):
                d[i][j] = min(d[i][j], d[i][k] + d[k][j])
    return d


N, P, K = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
d = [[float("inf")]*N for _ in range(N)]
for h in range(N):
    for w in range(N):
        if A[h][w] == -1:
            continue
        d[h][w] = A[h][w]

dd = warshall_floyd(d)
non_version = 0
for i in range(N-1):
    for j in range(i+1, N):
        if i == j:
            continue
        if dd[i][j] <= P:
            non_version += 1
if non_version == K:
    print('Infinity')
    exit()


def check(s: int):
    ok = 10**10
    ng = 0
    while 1 < ok-ng:
        mid = (ok+ng)//2
        d = [[float("inf")]*N for _ in range(N)]
        for h in range(N):
            for w in range(N):
                if A[h][w] == -1:
                    d[h][w] = mid
                else:
                    d[h][w] = A[h][w]
        dd = warshall_floyd(d)
        tmp = 0
        for i in range(N-1):
            for j in range(i+1, N):
                if i == j:
                    continue
                if dd[i][j] <= P:
                    tmp += 1
        if s < tmp:
            ng = mid
        else:
            ok = mid
    return ok


an_1 = check(K-1)
an_2 = check(K)
print(an_1-an_2)
