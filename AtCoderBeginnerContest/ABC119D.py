#https://atcoder.jp/contests/abc119/tasks/abc119_d

import bisect

a,b,q = map(int,input().split())
shrine = [-10**12, 10**12]
for _ in range(a):
    s = int(input())
    shrine.append(s)
shrine.sort()

temple = [-10**12, 10**12]
for _ in range(b):
    t = int(input())
    temple.append(t)
temple.sort()

for _ in range(q):
    x = int(input())
    sx = bisect.bisect_right(shrine,x)
    tx = bisect.bisect_right(temple,x)
    ans = 10**12
    #最適な経路はスタート地点から前後のshrine、templeを訪れる経路
    for i in [shrine[sx-1], shrine[sx]]:
        for j in [temple[tx-1], temple[tx]]:
            #caas_1はスタート→shrine→temple
            case_1 = abs(i-x)+abs(i-j)
            #caas_2はスタート→temple→shrine
            case_2 = abs(j-x)+abs(i-j)
            ans = min(ans,case_1,case_2)
            
    print(ans)
