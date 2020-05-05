#https://atcoder.jp/contests/agc015/tasks/agc015_b

s=list(input())

ans = 0

top_stair = len(s)

for i in range(len(s)):
    if s[i] == 'U':
        ans += top_stair-(i+1)
        ans += i*2
    else:
        ans += (top_stair-(i+1))*2
        ans += i
print(ans)
