#https://atcoder.jp/contests/abc057/tasks/abc057_d

import math
 
def combination(n, k):
    return math.factorial(n) // math.factorial(k) // math.factorial(n - k)

N,A,B = map(int,input().split())

V = list(map(int,input().split()))

v_count = {}

for v in V:
    if v not in v_count:
        v_count[v] = 1
    else:
        v_count[v] += 1

v_count = sorted(v_count.items(), key=lambda x:-x[0])

tmp_count = [0]
ans = 0
for val,count in v_count:
    tmp_count.append(tmp_count[-1]+count)
    if tmp_count[-1] < A:
        ans += val*count
    else:
        ans += val*(A-tmp_count[-2])
        print(ans/A)
        break
#print(tmp_count, ans)
if v_count[0][1] < A:
    comb = A-tmp_count[-2]
    root = combination(v_count[len(tmp_count)-2][1],comb)
else:
    root = 0
    for i in range(A, min(v_count[0][1],B)+1):
        root += combination(v_count[0][1],i)

print(root)
