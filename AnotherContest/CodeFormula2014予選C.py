# https://atcoder.jp/contests/code-formula-2014-qualb/tasks/code_formula_2014_qualB_c

from collections import Counter

A = input()
B = input()
len_A = len(A)
if "".join(sorted(A)) != "".join(sorted(B)):
    print('NO')
    exit()

diff_cnt = 0
nA = []
nB = []
for i in range(len_A):
    if A[i] != B[i]:
        diff_cnt += 1
        nA.append(A[i])
        nB.append(B[i])

if diff_cnt > 6:
    print('NO')
    exit()

cnt = Counter(A)
f = cnt.most_common(1)[0][1] == 1

if diff_cnt == 0 and not f:
    print('YES')
    exit()


def check(x: int):
    if f and x != 3:
        return
    if nA != nB:
        return
    print('YES')
    exit()


def dfs(n: int):
    if n == 4:
        return
    for i in range(diff_cnt):
        for j in range(diff_cnt):
            nA[i], nA[j] = nA[j], nA[i]
            check(n)
            dfs(n+1)
            nA[i], nA[j] = nA[j], nA[i]


dfs(1)
print('NO')
