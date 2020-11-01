# https://atcoder.jp/contests/abc181/tasks/abc181_d
# 8の倍数は下三桁が８の倍数かで判定(1-99までは別途判定)

S = input()
if int(S) < 10:
    S = int(S)
    if S%8==0:
        print('Yes')
    else:
        print('No')
elif int(S) < 100:
    SS = int(S[1]+S[0])
    if int(S)%8==0 or SS%8==0:
        print('Yes')
    else:
        print('No')
else:
    memo = []
    for i in range(100,1000):
        if i%8==0:
            memo.append(i)
    s_cnt = [0]*10
    for s in S:
        s = int(s)
        s_cnt[s] += 1

    for m in memo:
        tmp = {}
        for mm in str(m):
            mm = int(mm)
            if mm in tmp:
                tmp[mm] += 1
            else:
                tmp[mm] = 1
        ok_flag = True
        for key,val in tmp.items():
            if s_cnt[key] < val:
                ok_flag = False
                break
        if ok_flag:
            print('Yes')
            exit()
    print('No')