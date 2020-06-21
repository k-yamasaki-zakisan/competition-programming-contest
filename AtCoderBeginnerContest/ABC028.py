#https://atcoder.jp/contests/abc028/tasks/abc028_d

n,k = map(int,input().split())

ans = 0

#1回出現
ans += (n-k)*(k-1)*6

#2回出現
ans += (n-1)*3

#3回出現
ans += 1

print(ans/(n**3))
