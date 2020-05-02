#https://atcoder.jp/contests/abc148/tasks/abc148_e

n=int(input())

if n%2==1:
    print(0)
else:
    ans = 0
    memo = []
    bunbo = 10
    while bunbo <= n:
        memo.append(bunbo)
        bunbo *= 5
    for i in memo:
        ans += n//i
    print(ans)
