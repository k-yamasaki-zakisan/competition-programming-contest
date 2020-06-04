#https://atcoder.jp/contests/agc003/tasks/agc003_a

a=list(input())

n = 0

s = 0

e = 0

w = 0

for i in a:
  if i == 'N':
    n += 1
  elif i == 'S':
    s += 1
  elif i == 'E':
    e += 1
  elif i == 'W':
    w += 1

if n > 0 and s == 0 or n == 0 and s > 0 or e > 0 and w == 0 or e == 0 and w > 0:
  print('No')
else:
  print('Yes')
