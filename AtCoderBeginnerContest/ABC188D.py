# https://atcoder.jp/contests/abc188/tasks/abc188_d

# case1
N, C = map(int, input().split())
event = []
for i in range(N):
    a, b, c = map(int, input().split())
    a -= 1
    event.append((a, c))
    event.append((b, -c))
event.sort()
ans = 0
fee = 0
t = 0
for x, y in event:
    if x != t:
        ans += min(C, fee) * (x - t)
        t = x
    fee += y
print(ans)


# case2
N, C = map(int, input().split())
event = []
zahyo = []
for i in range(N):
    a, b, c = map(int, input().split())
    a -= 1
    event.append((a, c))
    event.append((b, -c))
    zahyo.append(a)
    zahyo.append(b)
event.sort()
zahyo.sort()

# 座標圧縮処理
*XS, = set(zahyo)
XS.sort()
zahyo = {e: i for i, e in enumerate(XS)}

max_dis = max(zahyo.values())
imos = [0]*(max_dis+1)
for i, cost in event:
    p = zahyo[i]
    imos[p] += cost
for i in range(1, len(imos)):
    imos[i] += imos[i-1]

ans = 0
for i in range(1, len(event)):
    ii, cost = event[i-1]
    p = zahyo[ii]
    ans += min(imos[p], C)*(event[i][0]-event[i-1][0])
print(ans)
