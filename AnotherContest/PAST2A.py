#https://atcoder.jp/contests/past202004-open/tasks/past202004_a

s,t = map(str,input().split())

if s[0] == t[0] or s[1] == t[1]:
  if s[0] == 'B':
    ans = abs(int(s[1])-int(t[1]))
  else:
    ans = abs(int(s[0])-int(t[0]))
else:
  if s[0] == 'B':
    ans = int(s[1])+int(t[0])-1
  else:
    ans = int(s[0])+int(t[1])-1

print(ans)
