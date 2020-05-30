#https://atcoder.jp/contests/nomura2020/tasks/nomura2020_b

s=list(input())

ans = []

for i in s:
  if i == '?':
    ans.append('D')
  else:
    ans.append(i)

print(''.join(map(str,ans)))
