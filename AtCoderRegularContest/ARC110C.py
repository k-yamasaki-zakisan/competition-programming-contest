# https://atcoder.jp/contests/arc110/tasks/arc110_c

N = int(input())
P = list(map(int,input().split()))
ans = []
tmp = []
num = 1
memo = []
for i,p in enumerate(P):
    if p == num:
        ans.append(p)
        ans += tmp
        tmp = [ans.pop()]
        [memo.append(j) for j in range(i,num-1,-1)]
        num = i+1
    else:
        tmp.append(p)
ans += tmp
for i,a in enumerate(ans):
    if i+1 != a:
        print(-1)
        exit()
if len(memo) < N-1:
    print(-1)
    exit()

for m in memo:
    print(m)