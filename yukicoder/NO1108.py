#https://yukicoder.me/problems/no/1108

n,h = map(int,input().split())

t = list(map(int,input().split()))

for i in range(n):
    t[i] += h

print(*t)
