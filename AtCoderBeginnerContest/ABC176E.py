#https://atcoder.jp/contests/abc176/tasks/abc176_e

H,W,M = map(int,input().split())
HW = [list(map(int, input().split())) for i in range(M)]
x = [0]*W
y = [0]*H
used = set()
for h,w in HW:
    h -= 1
    w -= 1
    y[h] += 1
    x[w] += 1
    used.add((h,w))

y_max = max(y)
x_max = max(x)
y_can = []
x_can = []
for i in range(H):
    if y[i] == y_max:
        y_can.append(i)
for i in range(W):
    if x[i] == x_max:
        x_can.append(i)

#候補地は爆弾があるり被りがあることを想定して-1しておく
ans = y_max+x_max-1
#print(ans, y_can,x_can)
flag = False
for yy in y_can:
    for xx in x_can:
        #print((yy,xx) in used,(yy,xx) ,used)
        if (yy,xx) in used:
            continue
        else:
            #候補地に爆弾がないことが確認できたので+1してループ抜け
            ans += 1
            flag = True
            break
    if flag:
        break
print(ans)
 
