# https://atcoder.jp/contests/past202012-open/tasks/past202012_e

H, W = map(int, input().split())
S = [list(input()) for _ in range(H)]
T = [list(input()) for _ in range(H)]

point = []
for h in range(H):
    for w in range(W):
        if T[h][w] == '#':
            point.append((h, w))

direction = [
    point,
    [(-j, i) for i, j in point],
    [(-i, -j) for i, j in point],
    [(j, -i) for i, j in point]
]
ans = False
for d in direction:
    for h in range(-20, 21):
        for w in range(-20, 21):
            ans |= all((0 <= i + h < H and 0 <= j + w <
                        W and S[i + h][j + w] == '.') for i, j in d)
if ans:
    print('Yes')
else:
    print('No')
