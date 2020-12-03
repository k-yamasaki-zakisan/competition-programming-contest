# https://atcoder.jp/contests/arc048/tasks/arc048_b

N = int(input())
RH = []
# 同レイトのジャンケン勝敗管理用配列
same_rate_group = [{1:0,2:0,3:0} for _ in range(100000+1)]
# レート別の勝敗管理用累積和配列
cnt_rate = [0]*(100000+1)
for _ in range(N):
    r,h = map(int,input().split())
    RH.append((r,h))
    same_rate_group[r][h] += 1
    cnt_rate[r] += 1

for i in range(1,len(cnt_rate)):
    cnt_rate[i] += cnt_rate[i-1]

ans = [[0]*3 for _ in range(N)]  
for i,rh in enumerate(RH):
    r,h = rh
    ans[i][0] += cnt_rate[r-1]
    ans[i][1] += cnt_rate[-1]-cnt_rate[r]
    ans[i][2] += same_rate_group[r][h]-1
    if h == 1:
        ans[i][0] += same_rate_group[r][2]
        ans[i][1] += same_rate_group[r][3]
    if h == 2:
        ans[i][0] += same_rate_group[r][3]
        ans[i][1] += same_rate_group[r][1]
    if h == 3:
        ans[i][0] += same_rate_group[r][1]
        ans[i][1] += same_rate_group[r][2]

for a in ans:
    print(*a)