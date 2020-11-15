# https://atcoder.jp/contests/past202005-open/tasks/past202005_f

N = int(input())
A = [list(input()) for _ in range(N)]

if N%2 == 1:
    center = A[N//2][0]
else:
    center = ''

side_l = side_r = ''
for i in range(N//2):
    moji_cnt = {}
    for a in A[i]:
        moji_cnt[a] = 1
    ng_flag = True
    for a in A[N-i-1]:
        if a in moji_cnt:
            side_l = side_l+a
            side_r = a+side_r
            ng_flag = False
            break
    if ng_flag:
        print(-1)
        exit()
print(side_l+center+side_r)