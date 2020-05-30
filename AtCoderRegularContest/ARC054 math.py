#https://atcoder.jp/contests/arc054/tasks/arc054_a

l,x,y,s,d = map(int,input().split())

if s <= d:
    tokei = abs(d-s)
    hantokei = l-abs(d-s)
else:
    tokei = l-abs(s-d)
    hantokei = abs(d-s)

tokei_time = tokei/(x+y)
hantokei_time = 10000000000
if y>x:
    hantokei_time = hantokei/(y-x)

print(min(tokei_time,hantokei_time))
