# https://atcoder.jp/contests/typical90/tasks/typical90_ch

MOD = 1000000007


def bit_zentansaku():
    ways = 0
    for i in range(1 << N):
        bit = [0]*20
        for j in range(N):
            bit[j + 1] = (i // (1 << j)) % 2
        flag = True
        for j in range(Q):
            if (((bit[x[j]] | bit[y[j]]) | bit[z[j]]) != w[j]):
                flag = False
        if flag:
            ways += 1
    return ways


N, Q = map(int, input().split())
x, y, z, w = [0]*100, [0]*100, [0]*100, [0]*100
XYZW = [list(map(int, input().split())) for _ in range(Q)]
ans = 1
for i in range(60):
    for j in range(Q):
        xyzw = XYZW[j]
        x[j] = xyzw[0]
        y[j] = xyzw[1]
        z[j] = xyzw[2]
        w[j] = (xyzw[3]//(1 << i)) % 2
    result = bit_zentansaku()
    ans *= result
    ans %= MOD
print(ans)
