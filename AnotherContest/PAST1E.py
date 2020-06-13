#https://atcoder.jp/contests/past201912-open/tasks/past201912_e

n,q = map(int,input().split())
dp = [['N' for i in range(n)] for j in range(n)]
for _ in range(q):
    t = list(map(int,input().split()))
    if t[0] == 1:
        dp[t[1]-1][t[2]-1] = 'Y'
    elif t[0] == 2:
        for i in range(n):
            if dp[i][t[1]-1] == 'Y':
                dp[t[1]-1][i] = 'Y'
    else:
        memo = []
        for i in range(n):
            if dp[t[1]-1][i] == 'Y':
                for j in range(n):
                    if dp[i][j] == 'Y' and t[1]-1 != j:
                        memo.append(j)
        for k in set(memo):
            dp[t[1]-1][k] = 'Y'
                    

for i in dp:
    print(''.join(map(str,i)))
