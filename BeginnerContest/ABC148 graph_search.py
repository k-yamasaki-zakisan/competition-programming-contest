#https://atcoder.jp/contests/abc148/tasks/abc148_f

def bfs(p):
    stack=[p]
    check = [-1]*n
    check[p] = 0
    while len(stack):
        v = stack.pop()
        for i in root[v]:
            if check[i] == -1:
                check[i]=check[v]+1
                stack.append(i)
    return check
    


n,u,v = map(int,input().split())
u -= 1
v -= 1
root = [[] for i in range(n)]
for _ in range(n-1):
    a, b = (int(x) for x in input().split())
    root[b-1].append(a-1)
    root[a-1].append(b-1)

move_count_u = bfs(u)
move_count_v = bfs(v)

ans = 0

for i in range(n):
    if move_count_u[i] < move_count_v[i]:
        ans = max(move_count_v[i]-1, ans)
print(ans)
