#問題
#https://atcoder.jp/contests/abc178/tasks/abc178_e
#参考
#https://naoyat.hatenablog.jp/entry/k-dimension-manhattan-distance

N = int(input())
plus = []
minus = []
for i in range(N):
    x,y = map(int,input().split())
    plus.append(x+y)
    minus.append(x-y)
plus.sort()
minus.sort()

ans_1 = plus[-1]-plus[0]
ans_2 = abs(minus[-1]-minus[0])
print(max(ans_1,ans_2))
