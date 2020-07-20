#https://atcoder.jp/contests/abc074/tasks/arc083_b

def warshall_floyd(d):
    for k in range(n):
        for i in range(n):
            for j in range(n):
                d[i][j] = min(d[i][j],d[i][k] + d[k][j])
    return d

import copy

n=int(input())
root = []
for _ in range(n):
    a = list(map(int,input().split()))
    root.append(a)

flag = True

for i in range(n):
    if root[i][i] != 0:
        flag = False
        break

search_distance = copy.deepcopy(root)

search_distance = warshall_floyd(search_distance)

ans = 0

for i in range(n):
    for j in range(n):
        if search_distance[i][j] != root[i][j]:
            flag = False
            break
        else:
            judge = 1
            for h in range(n):
                if h != i and h != j and root[i][h]+root[h][j] == root[i][j]:
                    judge = -1
            if judge == 1:
                ans += root[i][j]
if flag:
    print(ans//2)
else:
    print(-1)
