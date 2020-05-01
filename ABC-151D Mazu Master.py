#https://atcoder.jp/contests/abc151/tasks/abc151_d

import itertools
 
import copy
    
h,w = (int(x) for x in input().split())
ab = []
count = 0
for _ in range(h):
    a = input()
    a = a+'#'
    ab.append(list(a))
ab.append(list('#'*w))
mx = 0
 
for i in range(h):
    for j in range(w):
        if ab[i][j] == '.':
            dp = [[0 for a in range(w)] for b in range(h)]
            step = [[i, j]]
 
            while len(step) > 0:
                y, x = step.pop(0)
                if ab[y+1][x] == '.' and dp[y+1][x] == 0 :
                    step.append([y+1, x])
                    dp[y+1][x] = dp[y][x] + 1
                if ab[y][x+1] == '.' and dp[y][x+1] == 0 :
                    step.append([y, x+1])
                    dp[y][x+1] = dp[y][x] + 1
                if ab[y-1][x] == '.' and dp[y-1][x] == 0 :
                    step.append([y-1, x])
                    dp[y-1][x] = dp[y][x] + 1
                if ab[y][x-1] == '.' and dp[y][x-1] == 0 :
                    step.append([y, x-1])
                    dp[y][x-1] = dp[y][x] + 1
            dp[i][j] = 0
            mx = max([mx, max(list(itertools.chain.from_iterable(dp)))])
 
print(mx)
