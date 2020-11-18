# https://atcoder.jp/contests/arc002/tasks/arc002_2

def feb_check(N):
    if N%4 == 0:
        if N%100==0:
            if N%400==0:
                return 29
            else:
                return 28
        else:
            return 29
    else:
        return 28

    return 28

YMD = input()
Y = int(YMD[:4])
M = int(YMD[5:7])
D = int(YMD[8:])
limit_memo = {
    1:31,
    3:31,
    4:30,
    5:31,
    6:30,
    7:31,
    8:31,
    9:30,
    10:31,
    11:30,
    12:31
}
if M == 2:
    limit_day = feb_check(Y)
else:
    limit_day = limit_memo[M]

# 与えられた年月で探索
for d in range(D,limit_day+1):
    if Y%(d*M) == 0:
        print(f'{Y}/{str(M).zfill(2)}/{str(d).zfill(2)}')
        exit()

if M == 12:
    Y += 1
    M = 1
else:
    M += 1

# 割り切れるまでループして探索
while True:
    for m in range(M,13):
        if m == 2:
            limit_day = feb_check(Y)
        else:
            limit_day = limit_memo[m]
        for d in range(1,limit_day+1):
            if Y%(d*m) == 0:
                print(f'{Y}/{str(m).zfill(2)}/{str(d).zfill(2)}')
                exit()
    Y += 1
    M = 1