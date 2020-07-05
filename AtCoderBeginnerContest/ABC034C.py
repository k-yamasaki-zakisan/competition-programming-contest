#https://atcoder.jp/contests/abc034/tasks/abc034_c

#部分点
mod = 1000000007

w,h = map(int,input().split())

root = [[0 for i in range(w)] for j in range(h)] 

for i in range(h):
    for j in range(w):
        if i == 0 or j == 0:
            root[i][j] = 1
        else:
            root[i][j] = root[i-1][j]+root[i][j-1]
print(root[-1][-1]%mod)
