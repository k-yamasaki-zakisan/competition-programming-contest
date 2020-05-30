#https://atcoder.jp/contests/abc015/tasks/abc015_4

w = int(input())
n, k = [ int(v) for v in input().split() ]
dp_list = [ [ 0 for i in range (w+1) ] for i in range(k+1) ] 
dp_list[0][0] = 0
 
 
for _ in range(n):
    a, b = [ int(v) for v in input().split() ]
    for i in range(k-1, -1, -1):
        #print(dp_list)
        for j in range(w):
            #print(j)
            if j+a <= w:
                dp_list[i+1][j+a] = max(dp_list[i+1][j+a], dp_list[i][j] + b)
 
print(dp_list[-1][-1])
#print(dp_list)
