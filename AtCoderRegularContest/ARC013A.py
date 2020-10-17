# https://atcoder.jp/contests/arc013/tasks/arc013_1

n,m,l = map(int,input().split())
p,q,r = map(int,input().split())
ans = max(
    ((n//p)*(m//q)*(l//r)),
    ((n//q)*(m//p)*(l//r)),
    ((n//p)*(m//r)*(l//q)),
    ((n//q)*(m//r)*(l//p)),
    ((n//r)*(m//p)*(l//q)),
    ((n//r)*(m//q)*(l//p))
)

print(ans)