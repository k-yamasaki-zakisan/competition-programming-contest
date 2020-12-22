# https://atcoder.jp/contests/abc146/tasks/abc146_f

N, M = map(int, input().split())
S = input()
cnt_one = 0
# 到達可能問題か判定
for s in S:
    if s == '1':
        cnt_one += 1
    else:
        cnt_one = 0
    if cnt_one == M:
        print(-1)
        exit()

# ゴールから最も遠いジャンプ可能地点に移動を繰り返す
ans = []
step = N
goal_f = False
while step:
    for j in range(M, 0, -1):
        if step-j <= 0:
            ans.append(step)
            goal_f = True
            break
        if S[step-j] == '0':
            step -= j
            ans.append(j)
            break
    if goal_f:
        break

print(*ans[::-1])
