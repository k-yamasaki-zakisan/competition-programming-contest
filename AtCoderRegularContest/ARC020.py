#https://atcoder.jp/contests/arc020/tasks/arc020_2

import collections

n,c = map(int,input().split())
ab = []
for _ in range(n):
    a=int(input())
    ab.append(a)

gusu = []
kisu = []

for i in range(n):
  if i%2==0:
    kisu.append(ab[i])
  else:
    gusu.append(ab[i])

kisu = collections.Counter(kisu)
gusu = collections.Counter(gusu)

kisu = sorted(kisu.items(), key=lambda x:-x[1])
gusu = sorted(gusu.items(), key=lambda x:-x[1])

if kisu[0][0] == gusu[0][0]:
  if len(kisu)>1 and len(gusu)>1:
    ans = min(n-kisu[1][1]-gusu[0][1],n-kisu[0][1]-gusu[1][1])
    print(ans*c)
  elif len(kisu) == 1 and len(gusu) == 1:
    print(min(kisu[0][1],gusu[0][1])*c)
  elif len(kisu) == 1:
    print(min(n-kisu[0][1]-gusu[1][1],n-gusu[0][1])*c)
  elif len(gusu) == 1:
    print(min(n-gusu[0][1]-kisu[1][1],n-kisu[0][1])*c)
else:
  print((n-kisu[0][1]-gusu[0][1])*c)
