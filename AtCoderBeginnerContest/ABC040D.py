#https://atcoder.jp/contests/abc040/tasks/abc040_d

#部分点回答(重み付きグラフ)
from collections import deque

def graf_search(cost, start, border):
    move_count = 1
    d = [-1] * n
    d[start] = 1
    stack=deque([start])
    while stack:
        u = stack.popleft()
        for next_point, year in cost[u]:
            #print(next_point, year)
            if border < year and d[next_point] == -1:
                stack.append(next_point)
                d[next_point] = 1
                move_count += 1
    return move_count
    
n,m = map(int,input().split())
aby = [list(map(int, input().split())) for _ in range(m)]

q=int(input())
vw = [list(map(int, input().split())) for _ in range(q)]

#コスト表作成
cost = [[] for _ in range(n)]
for i, j, k in aby:
    cost[i - 1].append([j - 1, k])
    cost[j - 1].append([i - 1, k])

for v,w in vw:
    reselt = graf_search(cost, v - 1, w)
    print(reselt)
