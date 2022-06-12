# https://atcoder.jp/contests/abc255/tasks/abc255_e

from collections import defaultdict

n, m = map(int, input().split())
s = list(map(int, input().split()))
x = list(map(int, input().split()))

d = defaultdict(int)
b = 0
for i in range(n):
    for j in x:
        z = j - b
        if i % 2 == 0:
            z *= -1
        d[z] += 1
    if i != n - 1:
        b = s[i] - b
print(max(d.values()))
# print(d)
