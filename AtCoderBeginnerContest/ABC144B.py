#https://atcoder.jp/contests/abc144/tasks/abc144_b

n = int(input())

canFlag = False
for i in range(1,10):
    for j in range(1,10):
        if i*j==n:
            canFlag = True
if canFlag:
    print('Yes')
else:
    print('No')
