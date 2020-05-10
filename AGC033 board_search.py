#https://atcoder.jp/contests/agc033/tasks/agc033_a

import copy
import itertools
    
h,w = (int(x) for x in input().split())
ab = []
step = []
count = 0
for i in range(h):
    a = list(input())
    ab.append(a+['#'])
    for j in range(w):
        if a[j] == '#':
            step.append([i,j])

ab.append(list('#'*w))           
memo_step = copy.deepcopy(step)

dp = [[0 for a in range(w)] for b in range(h)]
 
while len(step) > 0:
    y, x = step.pop(0)
    if ab[y+1][x] == '.' and dp[y+1][x] == 0 and -1 < x < w and -1 < y < h :
        step.append([y+1, x])
        dp[y+1][x] = dp[y][x] + 1
    if ab[y][x+1] == '.' and dp[y][x+1] == 0 and -1 < x < w and -1 < y < h :
        step.append([y, x+1])
        dp[y][x+1] = dp[y][x] + 1
    if ab[y-1][x] == '.' and dp[y-1][x] == 0 and -1 < x < w and -1 < y < h :
        step.append([y-1, x])
        dp[y-1][x] = dp[y][x] + 1
    if ab[y][x-1] == '.' and dp[y][x-1] == 0 and -1 < x < w and -1 < y < h :
        step.append([y, x-1])
        dp[y][x-1] = dp[y][x] + 1

for i,j in memo_step:
    dp[i][j] = 0

mx = max(list(itertools.chain.from_iterable(dp)))
 
print(mx)
