# https://atcoder.jp/contests/abc153/tasks/abc153_f

from collections import deque
N,D,A = map(int,input().split())
XH = [list(map(int,input().split())) for _ in range(N)]
XH.sort()

pr = deque([])
dmg = ans = 0
for x,h in XH:
    # 範囲外となったダメージを削除する
    while len(pr) and pr[0][0] <= x:
        dmg -= pr[0][1]
        pr.popleft()
    # 範囲内で既に起きたダメージを受ける
    h -= dmg
    if h>0:
        new_count = h//A
        if h%A:
            new_count += 1
        ans += new_count
        dmg += A*new_count
        # 爆発が届く限界とそのダメージを記録
        pr.append([x+2*D+1,A*new_count])

print(ans)