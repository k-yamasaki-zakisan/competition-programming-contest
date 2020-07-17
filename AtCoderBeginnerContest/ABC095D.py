#https://atcoder.jp/contests/abc095/tasks/arc096_b

n,c=map(int,input().split())

xv=[]
xv_rev=[]

for _ in range(n):
    x,v=map(int,input().split())
    xv.append((x,v))
    xv_rev.append((c-x,v))

xv_rev=xv_rev[::-1]

right=[0]*n
right_re=[0]*n

sumv=0
#時計回り
for i,(x,v) in enumerate(xv):
    if i==0:
        sumv=v
        right[i]=max(0,sumv-x)
        right_re[i]=max(0,sumv-2*x)
    else:
        sumv+=v
        right[i]=max(right[i-1],sumv-x)
        right_re[i]=max(right_re[i-1],sumv-2*x)    

sumv=0
left=[0]*n
left_re=[0]*n

#反時計周り
for i,(x,v) in enumerate(xv_rev):
    if i==0:
        sumv=v
        left[i]=max(0,sumv-x)
        left_re[i]=max(0,sumv-2*x)
    else:
        sumv+=v
        left[i]=max(left[i-1],sumv-x)
        left_re[i]=max(left_re[i],sumv-2*x)    

ans=0
for i in range(n):
    if i==n-1:
        ans=max(ans,right[i])
        ans=max(ans,left[i])
    else:
        ans=max(ans,right[i]+left_re[n-i-2])
        ans=max(ans,left[i]+right_re[n-i-2])

print(ans)
