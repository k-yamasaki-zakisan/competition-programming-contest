# https://atcoder.jp/contests/abc259/tasks/abc259_e

from collections import defaultdict

nums_f = defaultdict(int)
nums_s = defaultdict(int)
N = int(input())
grand = []
for _ in range(N):
    M = int(input())
    pe = [list(map(int, input().split())) for _ in range(M)]
    grand.append(pe)
for pes in grand:
    for pe in pes:
        p, e = pe
        if nums_f[p] < e:
            nums_s[p] = nums_f[p]
            nums_f[p] = e
        else:
            nums_s[p] = max(nums_s[p], e)
cnt = 0
for i, pes in enumerate(grand):
    flag = True
    for j, pe in enumerate(pes):
        p, e = pe
        if nums_f[p] == e and nums_f[p] != nums_s[p]:
            flag = False
            break
    if flag:
        cnt += 1
print(N + 1 - cnt if cnt else N)
