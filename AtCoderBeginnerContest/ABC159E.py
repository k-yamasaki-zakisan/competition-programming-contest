# https://atcoder.jp/contests/abc159/tasks/abc159_e

from copy import copy
H, W, K = map(int, input().split())
S = []

for _ in range(H):
    line = input()
    s = []
    for num in line:
        num = int(num)
        s.append(num)
    S.append(s)

ans = 1001001
for i in range(2**(H-1)):
    c = []
    for j in range(H-1):
        if (i >> j & 1):
            c.append(j)
    stock = [0]*(len(c)+1)
    tmp = len(c)

    for w in range(W):
        now = [0]*(len(c)+1)
        index = 0
        for h in range(H):
            now[index] += S[h][w]
            if index == len(c):
                continue
            if h == c[index]:
                index += 1
        for l in range(len(c)+1):
            if K < now[l]:
                tmp = 10**10
                break
            if K < stock[l]+now[l]:
                stock = copy(now)
                tmp += 1
                break
            else:
                stock[l] += now[l]
    ans = min(ans, tmp)
print(ans)
