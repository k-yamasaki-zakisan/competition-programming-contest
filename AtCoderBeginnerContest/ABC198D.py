# https://atcoder.jp/contests/abc198/tasks/abc198_d

from itertools import permutations

A = input()
B = input()
C = input()
ABC = [A, B, C]
kind_alph = set()
for words in ABC:
    for word in words:
        kind_alph.add(word)

if 10 < len(kind_alph):
    print('UNSOLVABLE')
    exit()

list_kind_alph = list(kind_alph)
nums = range(10)
for v in permutations(nums, len(list_kind_alph)):
    flag = False
    for i in ABC:
        if v[list_kind_alph.index(i[0])] == 0:
            flag = True
            break
    if flag:
        continue
    N1 = N2 = N3 = ''
    for i in range(len(A)):
        N1 += str(v[list_kind_alph.index(A[i])])
    for i in range(len(B)):
        N2 += str(v[list_kind_alph.index(B[i])])
    for i in range(len(C)):
        N3 += str(v[list_kind_alph.index(C[i])])
    N1 = int(N1)
    N2 = int(N2)
    N3 = int(N3)
    if N1+N2 == N3:
        print(N1)
        print(N2)
        print(N3)
        exit()

print("UNSOLVABLE")
