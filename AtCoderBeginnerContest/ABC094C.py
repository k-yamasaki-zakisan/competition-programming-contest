#https://atcoder.jp/contests/abc094/tasks/arc095_a

import copy

n=int(input())

x = list(map(int,input().split()))

x2 = copy.copy(x)

x2.sort()

ans = [x2[n//2-1],x2[n//2]]

for xx in x:
    if xx <= ans[0]:
        print(ans[1])
    else:
        print(ans[0])
