#https://atcoder.jp/contests/donuts-2015/tasks/donuts_2015_3

N = int(input())

H = list(map(int,input().split()))

memo = []

for i in range(N):
    var =  H[i]
    print(len(memo))
    while 0 < len(memo):
        if memo[-1] < var:
            memo.pop()
        else:
            break
    memo.append(var)
