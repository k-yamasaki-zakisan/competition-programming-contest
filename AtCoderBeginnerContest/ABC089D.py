#https://atcoder.jp/contests/abc089/tasks/abc089_d

H,W,D = map(int,input().split())

max_value = H*W

position = [0]*(max_value+1)

root_cost = [0]*(max_value+1)

for y in range(H):
    A = list(map(int,input().split()))
    for x in range(W):
        position[A[x]] = (x+1,y+1)

for i in range(1,max_value+1):
    if 0 < i-D:
        x1,y1 = position[i-D]
        x2,y2 = position[i]
        root_cost[i] = root_cost[i-D]+(abs(x2-x1)+abs(y2-y1))

Q=int(input())

for i in range(Q):
    L,R = map(int,input().split())
    print(root_cost[R]-root_cost[L])
