#https://atcoder.jp/contests/tenka1-2019-beginner/tasks/tenka1_2019_c

n=int(input())

s=list(input())

black = [0]*n

white = [0]*n

for i in range(n):
    if s[i] == '.':
        white[i] = white[i-1]+1
        black[i] = black[i-1]
    else:
        white[i] = white[i-1]
        black[i] = black[i-1]+1
        
ans = 100000000

for i in range(n-1):
    if s[i] != s[i+1]:
        ans = min(ans,black[i]+(white[-1]-white[i+1]))
        
ans = min(ans,max(black),max(white))
print(ans)
