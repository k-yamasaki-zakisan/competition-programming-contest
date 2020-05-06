#https://atcoder.jp/contests/nikkei2019-qual/tasks/nikkei2019_qual_c

n=int(input())
ab = [[0, 0, 0] for i in range(n)]
for i in range(n):
    a, b = (int(x) for x in input().split())
    ab[i][0] = a+b
    ab[i][1] = a
    ab[i][2] = b

ab.sort(reverse=True)

ans = 0

for i in range(n):
    if i%2==0:
        ans += ab[i][1]
    else:
        ans -= ab[i][2]

print(ans)
