# https://atcoder.jp/contests/abc186/tasks/abc186_e

from math import gcd


def extgcd(a: int, b: int) -> list:
    if b:
        d, y, x = extgcd(b, a % b)
        y -= (a//b)*x
        return d, x, y
    return a, 1, 0


T = int(input())
for _ in range(T):
    N, S, K = map(int, input().split())
    g = gcd(K, N)
    if S % g != 0:
        print(-1)
        continue
    k = K//g
    n = N//g
    s = S//g

    g, x, y = extgcd(k, n)
    print(x*(-s) % n)
