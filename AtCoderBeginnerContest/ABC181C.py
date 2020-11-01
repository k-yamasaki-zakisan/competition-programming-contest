# https://atcoder.jp/contests/abc181/tasks/abc181_c
# ３点の全探索(3重ループ)して点の差を内積の法則で相似の関係か確認する

N = int(input())
XY = [list(map(int,input().split())) for _ in range(N)]
XY = sorted(XY, key=lambda x: x[1])
XY.sort()
for i in range(N-2):
    x1,y1 = XY[i]
    for j in range(i+1,N-1):
        x2,y2 = XY[j]
        for k in range(j+1,N):
            x3,y3 = XY[k]
            xm,ym = x2-x1,y2-y1
            xl,yl = x3-x1,y3-y1
            if xm*yl == ym*xl:
                print('Yes')
                exit()
print('No')