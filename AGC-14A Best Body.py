

n,s,t = map(int,input().split())

w=int(input())
if s <= w <= t:
    count = 1
else:
    count = 0

ab = []
for _ in range(n-1):
    a=int(input())
    w += a
    if s <= w <= t:
        count += 1
print(count)
