# https://atcoder.jp/contests/code-festival-2014-final/tasks/code_festival_final_c

N = int(input())
def f(x):
    strX = str(x)
    n = len(strX) - 1

    ans = 0
    for i,s in enumerate(strX):
        ans += int(s)*x**(n-i)
    return ans
L = []
for i in range(10, 10000+1):
    L.append(f(i))
if N in L:
    print(L.index(N)+10)
else:
    print(-1)