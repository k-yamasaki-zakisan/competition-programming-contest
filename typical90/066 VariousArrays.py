# https://atcoder.jp/contests/typical90/tasks/typical90_bn

N = int(input())
LR = []
cnt = 1
for _ in range(N):
    lr = list(map(int, input().split()))
    cnt *= (lr[-1]-lr[0]+1)
    LR.append(lr)

ans = 0
for i, lr in enumerate(LR):
    l, r = lr
    for j in range(l, r+1):
        for k in range(i):
            el, er = LR[k]
            if j < el:
                ans += cnt//(r-l+1)
            elif el <= j <= er:
                ans += (er-j)*cnt//(r-l+1)//(er-el+1)

print(ans/cnt)
