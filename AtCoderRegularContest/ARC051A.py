#https://atcoder.jp/contests/arc051/tasks/arc051_a

def circle_ckeck():
    if x2 <= x1-r and x1+r <= x3 and y2 <= y1-r and y1+r <= y3:
        print('NO')
    else:
        print('YES')

def dist(a,b):
    return a**2+b**2

def squre_check():
    #円の中にあるかどうかは(長方形の頂点と円の中心の距離)<=(円の半径)で判定
    if dist(x2-x1,y2-y1)<= r**2 and dist(x2-x1,y3-y1)<= r**2 and dist(x3-x1,y2-y1)<= r**2 and dist(x3-x1,y3-y1)<= r**2:
        print('NO')
    else:
        print('YES')

x1,y1,r = map(int,input().split())

x2,y2,x3,y3 = map(int,input().split())

circle_ckeck()

squre_check()
