#https://atcoder.jp/contests/abc160/tasks/abc160_e

x,y,a,b,c = map(int,input().split())

p = list(map(int,input().split()))

q = list(map(int,input().split()))

r = list(map(int,input().split()))

p.sort(reverse=True)

q.sort(reverse=True)

r.sort(reverse=True)

ans = []

for i in range(x):
    ans.append(p[i])

for i in range(y):
    ans.append(q[i])

ans = ans + r

ans.sort(reverse=True)

print(sum(ans[:x+y]))
