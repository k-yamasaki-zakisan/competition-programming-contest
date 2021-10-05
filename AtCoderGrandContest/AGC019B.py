# https://atcoder.jp/contests/agc019/tasks/agc019_b


from collections import defaultdict
memo = defaultdict(int)

A = input()
len_a = len(A)
all = len_a*(len_a-1)//2

for a in A:
    memo[a] += 1
tmp = 0
for val in memo.values():
    tmp += val*(val-1)//2
print(all-tmp+1)
