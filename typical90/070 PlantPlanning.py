# https: // atcoder.jp/contests/typical90/tasks/typical90_br

N = int(input())
X, Y = [], []
for _ in range(N):
    x, y = map(int, input().split())
    X.append(x)
    Y.append(y)
X.sort()
Y.sort()
x_mid = X[N//2]
y_mid = Y[N//2]
ans = 0
for i in range(N):
    x, y = X[i], Y[i]
    ans += abs(x-x_mid)
    ans += abs(y-y_mid)
print(ans)
