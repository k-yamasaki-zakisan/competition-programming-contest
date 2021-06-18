#
https: // atcoder.jp/contests/typical90/tasks/typical90_br
N = int(input())
X, Y = [], []
for _ in range(N):
    x, y = map(int, input().split())
    X.append(x)
    Y.append(y)

X.sort()
Y.sort()
nx, ny = (X[(N+1)//2-1]), (Y[(N+1)//2-1])
ans = 0
for i in range(N):
    x, y = X[i], Y[i]
    ans += abs(nx-x)+abs(ny-y)
print(ans)
