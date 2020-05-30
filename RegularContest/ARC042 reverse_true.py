#https://atcoder.jp/contests/arc042/tasks/arc042_a

N, M = map(int,input().split())
l = []
for i in range(M):
	l.append(int(input()))
l = l[::-1]
b = [False for i in range(N + 1)]
for li in l:
	if not b[li]:
		print(li)
		b[li] = True
for i in range(1, N + 1):
	if not b[i]:
		print(i)
		b[i] = True
