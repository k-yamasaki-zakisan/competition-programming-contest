#https://atcoder.jp/contests/abc173/tasks/abc173_c

import itertools

h,w,k = map(int,input().split())
ab = []
for _ in range(h):
    s=list(input())
    ab.append(s)

tate = []
yoko = []
 
for i in range(h):
    tate.append(i)

for i in range(w):
    yoko.append(i)

ans = 0

for i in range(h+1):
    for j in range(w+1):
        for v in itertools.combinations(tate, i):
            for vv in itertools.combinations(yoko, j):
                memo = 0
                for tt in range(h):
                    if tt in v:
                        continue
                    for yy in range(w):
                        if yy in vv:
                            continue
                        if ab[tt][yy] == '#':
                            memo += 1
                if memo == k:
                    ans += 1
print(ans)
