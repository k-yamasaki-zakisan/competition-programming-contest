#https://atcoder.jp/contests/cf17-final/tasks/cf17_final_c

N = int(input())
D = list(map(int,input().split()))
D.sort()
memo = []
for i in range(N):
    #左右に振り分けてなるべく離す
    if i%2==0:
        memo.append(D[i])
    else:
        memo.append(abs(24-D[i]))
memo.sort()
memo = [0]+memo+[24]
ans = 1000000000
for i in range(N+1):
    ans = min(ans, memo[i+1]-memo[i])
print(ans)
