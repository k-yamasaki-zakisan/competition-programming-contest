#https://atcoder.jp/contests/abc147/tasks/abc147_c

n=int(input())
a = [0]*20
x=[[0 for i in range(20)]for j in range(20)]
y=[[0 for i in range(20)]for j in range(20)]

for i in range(n):
	a[i]=int(input())
	for j in range(a[i]):
		x[i][j], y[i][j] = map(int,input().split())
		x[i][j]-=1

ans=0
for bits in range(1<<n):
	isok=True
	for i in range(n):
		if (bits>>i)&1 == 0:
			continue
		for j in range(a[i]):
			if y[i][j]^((bits>>x[i][j])&1):
				isok=False
	if isok:
		tmp=bits
		an=0
		while(tmp):
			if tmp&1:
				an+=1
			tmp//=2
		ans = max(ans,an)
print(ans)
