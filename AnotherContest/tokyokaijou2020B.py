#https://atcoder.jp/contests/tokiomarine2020/tasks/tokiomarine2020_b

a,v = map(int,input().split())

b,w = map(int,input().split())

t = int(input())

sa = abs(a-b)

tume = v-w

if tume*t < sa:
    print('NO')
else:
    print('YES')
