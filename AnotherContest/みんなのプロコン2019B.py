#https://atcoder.jp/contests/yahoo-procon2019-qual/tasks/yahoo_procon2019_qual_b

root = [[] for i in range(4)]
for _ in range(3):
    a,b = map(int,input().split())
    root[a-1].append(b-1)
    root[b-1].append(a-1)

visited = [False] * 4
visited[0] = True

def dfs(s):
    if all(visited):
        print('YES')
        exit()

    for i in root[s]:
        if visited[i]:
            continue

        visited[i] = True
        dfs(i)
        visited[i] = False

dfs(0)
print('NO')
