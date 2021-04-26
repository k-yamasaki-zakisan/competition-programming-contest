# https://atcoder.jp/contests/typical90/tasks/typical90_j

N = int(input())
CP = [list(map(int, input().split())) for _ in range(N)]
Q = int(input())
LR = [list(map(int, input().split())) for _ in range(Q)]
f_class = [0]*N
s_class = [0]*N
for i, cp in enumerate(CP):
    c, p = cp
    f_class[i] += f_class[i-1]
    s_class[i] += s_class[i-1]
    if c == 1:
        f_class[i] += p
    else:
        s_class[i] += p

for l, r in LR:
    l, r = l-1, r-1
    if l != 0:
        ans_f, ans_s = f_class[r]-f_class[l-1], s_class[r]-s_class[l-1]
    else:
        ans_f, ans_s = f_class[r], s_class[r]
    print(ans_f, ans_s)
