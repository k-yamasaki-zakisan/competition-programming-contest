#https://atcoder.jp/contests/code-festival-2015-qualb/tasks/codefestival_2015_qualB_b


n,m = map(int,input().split())

a = list(map(int,input().split()))

memo = [0]*(m+1)

for i in a:
   memo[i] += 1

if max(memo) > n//2:
    print(memo.index(max(memo)))
else:
    print('?')
