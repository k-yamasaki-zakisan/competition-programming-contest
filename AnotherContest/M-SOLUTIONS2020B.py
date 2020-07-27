#https://atcoder.jp/contests/m-solutions2020/tasks/m_solutions2020_b

a,b,c = map(int,input().split())

k=int(input())   

count = 0

while b <= a:
    b *= 2
    count += 1

while c <= b:
    c *= 2
    count += 1

if count <= k:
    print('Yes')
else:
    print('No')
