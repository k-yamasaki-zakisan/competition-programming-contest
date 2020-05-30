#https://atcoder.jp/contests/sumitrust2019/tasks/sumitb2019_e

a=int(input())
b=list(map(int,input().split()))
c=[0,0,0]
ans=1
mod=1000000007
for i in b:
  d=0
  for j in c:
    if i==j:
      d+=1
  if d==0:
    ans = 0
    break
  else:
    ans=ans*d%mod
    for j in range(3):
      if i==c[j]:
        c[j]+=1
        break
print(ans)
