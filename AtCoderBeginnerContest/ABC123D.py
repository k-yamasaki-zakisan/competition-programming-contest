#https://atcoder.jp/contests/abc123/tasks/abc123_d

x,y,z,k = map(int,input().split())

a = list(map(int,input().split()))

b = list(map(int,input().split()))

c = list(map(int,input().split()))

mid = []

for i in range(x):
    for j in range(y):
        mid.append(a[i]+b[j])

mid.sort(reverse=True)

ans = []

for i in range(min(k,len(mid))):
    for j in range(z):
        ans.append(mid[i]+c[j])

ans.sort(reverse=True)

for i in range(k):
    print(ans[i])
