#https://atcoder.jp/contests/chokudai_S001/tasks/chokudai_S001_i

n = int(input())

t = list(map(int,input().split()))

tmp = 0

front = 0

ans = 0

for i,val in enumerate(t):
    tmp += val
    while n < tmp and front < n:
        tmp -= t[front]
        front += 1
    if tmp == n:
        ans += 1
print(ans)
