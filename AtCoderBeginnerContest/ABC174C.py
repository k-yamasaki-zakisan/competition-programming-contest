#https://atcoder.jp/contests/abc174/tasks/abc174_c

n=int(input())

x = 0

for i in range(n+1):
    x = x*10+7
    x %= n
    if x == 0:
        print(i+1)
        exit()
    #print(x)
print(-1)
