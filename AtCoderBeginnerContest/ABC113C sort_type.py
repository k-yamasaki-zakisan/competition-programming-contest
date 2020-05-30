#https://atcoder.jp/contests/abc113/tasks/abc113_c

n,m = map(int,input().split())
py = []
p_y = [[] for i in range(n)]
for _ in range(m):
    p,y = map(int,input().split())
    py.append((p,y))
    p_y[p-1].append(y)
ans = {}
for i, tmp in enumerate(p_y):
    cnt = 1
    p_y[i] = tmp.sort()
    for j, jj in enumerate(tmp):
 
        ans[(i+1, jj)] = str(i+1).zfill(6) + str(j+1).zfill(6)
 
 
for i, tmp in enumerate(py):
    print(ans[tmp])
