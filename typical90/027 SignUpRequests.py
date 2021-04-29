# https://atcoder.jp/contests/typical90/tasks/typical90_aa

N = int(input())
S = [input() for _ in range(N)]
names = set()
for i, s in enumerate(S):
    ex_len = len(names)
    names.add(s)
    if ex_len + 1 == len(names):
        print(i+1)
