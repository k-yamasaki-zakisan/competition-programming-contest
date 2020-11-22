# https://atcoder.jp/contests/abc184/tasks/abc184_e

from collections import deque

H,W = map(int,input().split())
A = []
stack = deque([])
alf_woop = {}
dp = [[-1]*W for _ in range(H)]
for h in range(H):
    a = list(input())
    A.append(a)
    for w in range(W):
        if a[w] == 'S':
            stack.append([h,w])
            dp[h][w] = 0
        elif a[w] == 'G':
            goal = [h,w]
        elif a[w] != '.':
            if a[w] in alf_woop:
                alf_woop[a[w]].append([h,w])
            else:
                alf_woop[a[w]] = [[h,w]]

while len(stack):
    h,w = stack.popleft()
    if goal == [h,w]:
        print(dp[h][w])
        exit()
    for y,x in [[1,0],[-1,0],[0,1],[0,-1]]:
        nh, nw = h+y, w+x
        if 0 <= nh < H and 0 <= nw < W and A[nh][nw] != '#' and dp[nh][nw] == -1:
            dp[nh][nw] = dp[h][w]+1
            stack.append([nh,nw])
    if A[h][w] in alf_woop:
        for nh,nw in alf_woop[A[h][w]]:
            if dp[nh][nw] == -1:
                dp[nh][nw] = dp[h][w]+1
                stack.append([nh,nw])
        alf_woop.pop(A[h][w])
print(-1)