#https://yukicoder.me/problems/no/1133

n,m = map(int,input().split())

s = list(input())

memo = [[1]*(n+1) for i in range(n+1)]

memo[0][0] = 0

y, x = 0, 0

for i in range(m):
    if s[i] == 'U':
        y += 1
    elif s[i] == 'D':
        y -= 1
    elif s[i] == 'R':
        x += 1
    elif s[i] == 'L':
        x -= 1
    memo[y][x] = 0

for i in range(n,-1,-1):
    print(*memo[i])
