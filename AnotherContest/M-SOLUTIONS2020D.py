#https://atcoder.jp/contests/m-solutions2020/tasks/m_solutions2020_d

n = int(input())

a = list(map(int,input().split()))

money = 1000

for i in range(1,n):
    if a[i-1] < a[i]:
        money = money%a[i-1]+a[i]*(money//a[i-1])

print(money)
