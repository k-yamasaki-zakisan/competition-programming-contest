# https://atcoder.jp/contests/typical90/tasks/typical90_bn

N = int(input())
LR = [list(map(int, input().split())) for _ in range(N)]

ans = 0
for i in range(N):
    li, ri = LR[i]
    tmp = 0
    for j in range(li, ri+1):
        for k in range(i):
            lk, rk = LR[k]
            if j <= rk:
                tmp += (rk-max(j, lk-1))/(rk-lk+1)
    ans += tmp/(ri-li+1)
print(ans)
