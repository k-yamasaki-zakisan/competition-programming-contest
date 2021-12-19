# https://atcoder.jp/contests/abc232/tasks/abc232_e

MOD = 998244353


H, W, K = map(int, input().split())
x1, y1, x2, y2 = map(int, input().split())
if x1 == x2 and y1 == y2:
    diff_xy, same_y, same_x, same_xy = 0, 0, 0, 1
elif x1 == x2:
    diff_xy, same_y, same_x, same_xy = 0, 0, 1, 0
elif y1 == y2:
    diff_xy, same_y, same_x, same_xy = 0, 1, 0, 0
else:
    diff_xy, same_y, same_x, same_xy = 1, 0, 0, 0
for _ in range(K-2):
    n_diff_xy = diff_xy*(H-2+W-2)+same_x*(H-1)+same_y*(W-1)
    n_diff_xy %= MOD
    n_same_y = diff_xy+same_y*(H-2)+same_xy*(H-1)
    n_same_y %= MOD
    n_same_x = diff_xy+same_x*(W-2)+same_xy*(W-1)
    n_same_x %= MOD
    n_same_xy = same_x+same_y
    n_same_xy %= MOD

    diff_xy = n_diff_xy
    same_y = n_same_y
    same_x = n_same_x
    same_xy = n_same_xy
#print(diff_xy, same_y, same_x, same_xy)
ans = diff_xy*2+same_y*(H-2)+same_x*(W-2)+same_xy*(H-1+W-1)
print(ans % MOD)
