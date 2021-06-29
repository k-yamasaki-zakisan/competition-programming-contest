# https://atcoder.jp/contests/typical90/tasks/typical90_ca

H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]
B = [list(map(int, input().split())) for _ in range(H)]
ans = 0
for h in range(H-1):
    for w in range(W-1):
        diff = B[h][w]-A[h][w]
        ans += abs(diff)
        for y, x in [[0, 0], [1, 0], [0, 1], [1, 1]]:
            A[h+y][w+x] += diff

is_same = True
for h in range(H):
    for w in range(W):
        if A[h][w] != B[h][w]:
            is_same = False
if is_same:
    print('Yes')
    print(ans)
else:
    print('No')
