#https://atcoder.jp/contests/arc035/tasks/arc035_b

import math
import collections

mod = 1000000007

n=int(input())
ab = []
for _ in range(n):
    a = int(input())
    ab.append(a)

#ペナルティ最低値の算出
ab.sort()

total_time = 0

penalty = 0

for i in ab:
    total_time += i
    penalty += total_time

print(penalty)

#ペナルティ最低値の選びかたを算出
penalty_root = 1
c = collections.Counter(ab)
type_counter = sorted(c.items(), key=lambda x:-x[1])
for key,val in type_counter:
    penalty_root *= math.factorial(val)
    penalty_root %= mod

print(penalty_root)
