# https://atcoder.jp/contests/typical90/tasks/typical90_b

N = int(input())
ans = []
for bits in range(1 << N):
    tmp = ''
    cnt = 0
    for i in range(N):
        if (bits >> i) & 1 == 0:
            tmp += ')'
            cnt -= 1
        else:
            tmp += '('
            cnt += 1
        if cnt < 0:
            break
    if cnt == 0:
        ans.append(tmp)

ans.sort()
for a in ans:
    print(a)
