#https://atcoder.jp/contests/code-festival-2015-qualb/tasks/codefestival_2015_qualB_c

n,m = map(int,input().split())

a = list(map(int,input().split()))

b = list(map(int,input().split()))

if n < m:
    print('NO')
else:
    a.sort(reverse=True)
    b.sort(reverse=True)
    for i in range(m):
        if a[i] < b[i]:
            print('NO')
            exit()
    print('YES')
