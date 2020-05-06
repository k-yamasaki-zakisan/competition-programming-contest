#https://atcoder.jp/contests/dwango2016-prelims/tasks/dwango2016qual_b


n=int(input())

t = list(map(int,input().split()))

ans = [t[0]]

for i in range(n-2):
    ans.append(min(t[i],t[i+1]))

ans.append(t[-1])

print(*ans)
