#https://atcoder.jp/contests/arc036/tasks/arc036_b

n=int(input())
ab = []
for _ in range(n):
    a=int(input())
    ab.append(a)

left = [1]

count = 1

for i in range(1,n):
  if ab[i] > ab[i-1]:
    count += 1
  else:
    count = 1
  left.append(count)

right = [0]*n

count = 1

right[-1] = count

for i in range(2,n+1):
  if ab[-i] > ab[-i+1]:
    count += 1
  else:
    count = 1
  right[-i] = count

yama = 0

for i in range(n):
  yama = max(yama, left[i]+right[i]-1)

print(yama)
    
