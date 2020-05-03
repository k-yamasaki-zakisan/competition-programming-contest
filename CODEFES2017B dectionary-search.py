#https://atcoder.jp/contests/code-festival-2017-qualb/tasks/code_festival_2017_qualb_b

from collections import Counter
 
N = int(input())
D = list(input().split())
 
M = int(input())
T = list(input().split())
 
D_count = Counter(D)
T_count = Counter(T)

for k, v in T_count.items():
    if D_count[k] < v:
        print('NO')
        exit()
 
print('YES')
