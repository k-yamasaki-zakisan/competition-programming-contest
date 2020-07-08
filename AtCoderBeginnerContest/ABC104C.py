#https://atcoder.jp/contests/abc104/tasks/abc104_c

import itertools

D,G = map(int,input().split())
ab = []
for _ in range(D):
    p, c = (int(x) for x in input().split())
    ab.append([p,c])

ans = 10000000

pick_num = []

for i in range(D):
    pick_num.append(i)

for i in range(0,D+1):
    for v in itertools.combinations(pick_num, i):      
        tmp_point = 0
        tmp_count = 0
        for j in v:
            tmp_point += ab[j][0]*(j+1)*100+ab[j][1]
            tmp_count += ab[j][0]
        if tmp_point < G:
            nokori = G-tmp_point
            for k in range(D-1, -1,-1):
                if k not in v:
                    if nokori%(100*(k+1)) == 0:
                        if nokori//(100*(k+1)) < ab[k][0]:
                            tmp_count += nokori//(100*(k+1))
                            tmp_point += nokori
                    else:
                        if nokori//(100*(k+1))+1 < ab[k][0]:
                            tmp_count += nokori//(100*(k+1))+1
                            tmp_point += nokori
                    break
        if G <= tmp_point:
            ans = min(ans, tmp_count)
print(ans)
