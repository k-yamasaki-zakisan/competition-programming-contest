#https://atcoder.jp/contests/abc023/tasks/abc023_d

#最低高度を二分探索で決める
N = int(input())
H = []
S = []
for i in range(N):
    h, s = map(int,input().split())
    H.append(h)
    S.append(s)

ok = 10**14
ng = 0

while (abs(ok - ng) > 1):
    mid = (ok+ng)//2
    check = []
    flag = True
    for i in range(N):
        check.append((mid-H[i])//S[i])
    check.sort()
    for j in range(N):
        if check[j] < j:
            flag = False
    if flag:
        ok = mid
    else:
        ng = mid

print(ok)
