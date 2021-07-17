# https://atcoder.jp/contests/typical90/tasks/typical90_bb

N, M = map(int, input().split())
R = [[] for _ in range(M)]
for i in range(M):
    _ = input()
    R[i] = list(map(int, input().split()))

flag = [1]*M
near = [[] for _ in range(N)]
for i in range(M):
    for p in R[i]:
        near[p-1].append(i)

ans = [-1]*N
ans[0] = 0
que = [0]
for q in que:
    lst = []
    for i in near[q]:
        if flag[i]:
            lst += R[i]
            flag[i] = 0
    for p in lst:
        if ans[p-1] < 0:
            que.append(p-1)
            ans[p-1] = ans[q] + 1
print(*ans, sep='\n')
