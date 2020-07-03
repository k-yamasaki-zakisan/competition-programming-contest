#https://atcoder.jp/contests/abc159/tasks/abc159_d

n=int(input())

t = list(map(int,input().split()))

memo = [0]*(2*10**5+1)

for i in t:
    memo[i] += 1

ans = 0

for i in memo:
    ans += i*(i-1)//2

for i in t:
    print(ans-(memo[i]*(memo[i]-1)//2)+((memo[i]-1)*(memo[i]-2)//2))
    
