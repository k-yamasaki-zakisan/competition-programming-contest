# https://atcoder.jp/contests/abc109/tasks/abc109_d
# 方針：とりあえず奇数のマスは１つ横に数を渡す、横端の場合は下に１を渡す、右下の角の場合はステイでAC

H,W = map(int,input().split())
A = [list(map(int,input().split())) for _ in range(H)]
ans = []
for h in range(H):
    for w in range(W):
        if A[h][w]%2:
            if w == W-1:
                if h != H-1:
                    A[h+1][w] += 1
                    A[h][w] -= 1
                    ans.append([h+1,w+1,h+2,w+1])
            else:
                A[h][w+1] += 1
                A[h][w] -= 1
                ans.append([h+1,w+1,h+1,w+2])
print(len(ans))
for an in ans:
    print(*an)