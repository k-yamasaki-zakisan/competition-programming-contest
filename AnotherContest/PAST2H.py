#https://atcoder.jp/contests/past202004-open/tasks/past202004_h

n,m = (int(x) for x in input().split())
ab = []
count = 0
dp = [[-1 for a in range(m)] for b in range(n)]
for i in range(n):
    a = list(input())
    ab.append(a)
    for j in range(m):
        if a[j] == 'S':
            step = [[i,j]]
            dp[i][j] = 0
count = 1

move = [[1,0],[0,1],[-1,0],[0,-1]]
 
while len(step) > 0:
    #print(step)
    y, x = step.pop(0)
    for yy, xx in move:
        if 0 <= y+yy <= n-1 and 0 <= x+xx <= m-1:
            if dp[y+yy][x+xx] == -1:
                dp[y+yy][x+xx] = dp[y][x]+1
                step.append([y+yy,x+xx])
                if str(count) == ab[y+yy][x+xx]:
                    memo = dp[y+yy][x+xx]
                    dp = [[-1 for a in range(m)] for b in range(n)]
                    dp[y+yy][x+xx] = memo
                    count += 1
                    step = []
                    step = [[y+yy,x+xx]]
                    break
                elif count == 10 and ab[y+yy][x+xx] == 'G':
                    print(dp[y+yy][x+xx])
                    exit()
 
print(-1)
