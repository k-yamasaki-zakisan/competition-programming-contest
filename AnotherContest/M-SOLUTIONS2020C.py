#https://atcoder.jp/contests/m-solutions2020/tasks/m_solutions2020_c

n,k = map(int,input().split())

a = list(map(int,input().split()))


for i in range(k, n+1):
    if i == n:
        break
    #print(a[i], a[i-k])
    if a[i-k] < a[i]:
        print('Yes')
    else:
        print('No')
