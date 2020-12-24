# https://atcoder.jp/contests/arc025/tasks/arc025_2

H, W = map(int, input().split())
C = [list(map(int, input().split())) for _ in range(H)]

Black = [[0]*W for _ in range(H)]
White = [[0]*W for _ in range(H)]
for h in range(H):
    for w in range(W):
        if h % 2:
            if w % 2:
                Black[h][w] = C[h][w]
            else:
                White[h][w] = C[h][w]
        else:
            if w % 2:
                White[h][w] = C[h][w]
            else:
                Black[h][w] = C[h][w]

Black_c = [[0]*(W+1) for _ in range(H+1)]
White_c = [[0]*(W+1) for _ in range(H+1)]

for h in range(H):
    for w in range(W):
        Black_c[h+1][w+1] = Black_c[h][w+1] + \
            Black_c[h+1][w]-Black_c[h][w]+Black[h][w]
        White_c[h+1][w+1] = White_c[h][w+1] + \
            White_c[h+1][w]-White_c[h][w]+White[h][w]

ans = 0
for lh in range(H+1):
    for hh in range(lh):
        for right in range(W+1):
            for left in range(right):
                black = Black_c[hh][left]+Black_c[lh][right] - \
                    Black_c[hh][right] - Black_c[lh][left]
                white = White_c[hh][left]+White_c[lh][right] - \
                    White_c[hh][right] - White_c[lh][left]
                print(black, white)
                if white == black:
                    ans = max(ans, (lh-hh)*(right-left))
print(ans)
