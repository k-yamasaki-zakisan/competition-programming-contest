# https://atcoder.jp/contests/typical90/tasks/typical90_al

import math


def lcm(x, y):
    return (x * y) // math.gcd(x, y)


A, B = map(int, input().split())
ans = lcm(A, B)
if ans <= 10**18:
    print(ans)
else:
    print('Large')
