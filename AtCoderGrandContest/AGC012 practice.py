#https://atcoder.jp/contests/agc012/tasks/agc012_a

n=int(input())

t = list(map(int,input().split()))

t.sort(reverse=True)

ans = 0

for i in range(n,n+n):
    ans += t[i]
print(ans)
