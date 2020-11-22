# https://atcoder.jp/contests/arc005/tasks/arc005_2

X,Y,W = map(str,input().split())
x,y = int(X)-1,int(Y)-1
C = [list(input()) for _ in range(9)]
hoko = {
    # [y,x]方向
    'R':[0,1],
    'L':[0,-1],
    'U':[-1,0],
    'D':[1,0],
    'RU':[-1,1],
    'RD':[1,1],
    'LU':[-1,-1],
    'LD':[1,-1]
}
ans = C[y][x]
my,mx = hoko[W]
for _ in range(3):
    if y+my < 0 or 8 < y+my:
        my *= -1
    if x+mx < 0 or 8 < x+mx:
        mx *= -1
    y += my
    x += mx
    ans += C[y][x]
print(ans)