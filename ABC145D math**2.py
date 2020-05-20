#https://atcoder.jp/contests/abc145/tasks/abc145_d

x,y = map(int,input().split())
mod =10**9+7
 
a=(-x+2*y)//3
b=(2*x-y)//3
n=a+b
 
def fact(x,p):
    ret=1
    for i in range(1,x+1):
        ret*=i
        ret%=p
    return ret
 
 
if a+2*b==x and b+2*a==y and a>=0 and b>=0:
    ans=fact(n,mod) * pow(fact(b,mod),mod-2,mod)*pow(fact(a,mod),mod-2,mod)
    print(ans%mod)
else:
    print("0")
