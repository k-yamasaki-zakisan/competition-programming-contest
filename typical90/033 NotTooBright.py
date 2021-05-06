# https://atcoder.jp/contests/typical90/tasks/typical90_ag

H, W = map(int, input().split())
t = H//2 if H % 2 == 0 else H//2 + 1
y = W//2 if W % 2 == 0 else W//2 + 1
ans = t * y
# 謎のコーナーケース
if H == 1 or W == 1:
    print(H*W)
    exit()
print(ans)
