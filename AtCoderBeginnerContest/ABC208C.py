# https://atcoder.jp/contests/abc218/tasks/abc218_c

N = int(input())
S = [input() for _ in range(N)]
T = [input() for _ in range(N)]
T_list = []
cnt_t = cnt_s = 0
for h in range(N):
    for w in range(N):
        if T[h][w] == '#':
            T_list.append((h, w))
            cnt_t += 1
        if S[h][w] == '#':
            cnt_s += 1
if cnt_t != cnt_s:
    print('No')
    exit()

fy, fx = T_list[0]

b_flag = False
ok_glag = True
for h in range(N):
    for w in range(N):
        if S[h][w] == '#':
            b_flag = True
            diff_y, diff_x = h-fy, w-fx
            for ht, wt in T_list:
                ck_h, ch_w = diff_y+ht, diff_x+wt
                if not(0 <= ck_h < N and 0 <= ch_w < N and S[ck_h][ch_w] == '#'):
                    ok_glag = False
                    break
            break
    if b_flag:
        break
if ok_glag:
    print('Yes')
    exit()

# 90度右回転
tmp_90_right = []
for xy in zip(*S[::-1]):
    tmp_90_right.append(xy)

b_flag = False
ok_glag = True
for h in range(N):
    for w in range(N):
        if tmp_90_right[h][w] == '#':
            b_flag = True
            diff_y, diff_x = h-fy, w-fx
            for ht, wt in T_list:
                ck_h, ch_w = diff_y+ht, diff_x+wt
                if not(0 <= ck_h < N and 0 <= ch_w < N and tmp_90_right[ck_h][ch_w] == '#'):
                    ok_glag = False
                    break
            break
    if b_flag:
        break
if ok_glag:
    print('Yes')
    exit()

# 90度左回転
tmp_90_left = []
T_S = list(zip(*S))
for x in T_S[::-1]:
    tmp_90_left.append(x)

ok_glag = True
b_flag = False
for h in range(N):
    for w in range(N):
        if tmp_90_left[h][w] == '#':
            b_flag = True
            diff_y, diff_x = h-fy, w-fx
            for ht, wt in T_list:
                ck_h, ch_w = diff_y+ht, diff_x+wt
                if not(0 <= ck_h < N and 0 <= ch_w < N and tmp_90_left[ck_h][ch_w] == '#'):
                    ok_glag = False
                    break
            break
    if b_flag:
        break
if ok_glag:
    print('Yes')
    exit()

# 180回転
tmp_180 = []
T_S = [s[::-1] for s in S]
for x in T_S[::-1]:
    tmp_180.append(x)

ok_glag = True
b_flag = False
for h in range(N):
    for w in range(N):
        if tmp_180[h][w] == '#':
            b_flag = True
            diff_y, diff_x = h-fy, w-fx
            for ht, wt in T_list:
                ck_h, ch_w = diff_y+ht, diff_x+wt
                if not(0 <= ck_h < N and 0 <= ch_w < N and tmp_180[ck_h][ch_w] == '#'):
                    ok_glag = False
                    break
            break
    if b_flag:
        break
if ok_glag:
    print('Yes')
    exit()
print('No')
