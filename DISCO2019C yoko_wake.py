#https://atcoder.jp/contests/ddcc2020-qual/tasks/ddcc2020_qual_c

h,w,k = map(int,input().split())
ab = []
check_y = []
check_y1 = []
for i in range(h):
    a = list(input())
    ab.append(a)
    flag = True
    for j in a:
        if j == '#':
            flag = False
            break
    if flag:
        check_y.append(i)

count = 0
dp = [[0 for a in range(w)] for b in range(h)]

for y in range(h):
    if y in check_y:
        for x in range(w):
            dp[y][x] = dp[y-1][x]
    else:
        count += 1
        counti = 0
        for x in range(w):
            if ab[y][x] == '#':
                counti += 1
                if counti > 1:
                    count += 1
            dp[y][x] = count
if dp[0][0] == 0:
    for i in range(h):
        if dp[i][0] == 1:
            memo = i
            break
    for y in range(memo):
        for x in range(w):
            dp[y][x] = dp[memo][x]
            
for s in dp:
    print(*s)
