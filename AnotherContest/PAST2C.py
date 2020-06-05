#https://atcoder.jp/contests/past202004-open/submissions/me

n=int(input())
ab = []
for _ in range(n):
    s=list(input())
    ab.append(s)

for i in range(n-2,-1,-1):
  for j in range(n*2-1):
    if ab[i][j] == '#':
      if j == 0:
        if ab[i+1][j] == 'X' or ab[i+1][j+1] == 'X':
          ab[i][j] = 'X'
      elif j == n*2-2:
        if ab[i+1][j-1] == 'X' or ab[i+1][j] == 'X':
          ab[i][j] = 'X'
      else:
        if ab[i+1][j-1] == 'X' or ab[i+1][j] == 'X' or ab[i+1][j+1] == 'X':
          ab[i][j] = 'X'

for i in ab:
  print(''.join(map(str,i)))
