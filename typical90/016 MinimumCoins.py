# https://atcoder.jp/contests/typical90/tasks/typical90_p

N = int(input())
A, B, C = map(int, input().split())
ans = 10**10
for i in range(10000):
    for j in range(10000-i):
        CN = N-(A*i+B*j)
        if CN < 0:
            break
        if CN % C == 0:
            ans = min(ans, i+j+CN//C)
print(ans)
