#https://atcoder.jp/contests/agc032/tasks/agc032_a



n=int(input())

ball = list(map(int,input().split()))

ans = []

count = 0

while len(ball)>0:
    count += 1
    for i in range(len(ball)-1,-1,-1):
        #print(ball,i)
        if i+1 ==ball[i]:
            move = ball.pop(i)
            ans.insert(0,move)
            break
    if count ==100000:
        break
    

if len(ans) == n:
    for i in ans:
        print(i)
else:
    print(-1)
