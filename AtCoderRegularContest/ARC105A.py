#https://atcoder.jp/contests/arc105/tasks/arc105_a

item = list(map(int,input().split()))

for i in range(2 ** 4):
    bag = []
    for j in range(4):  # このループが一番のポイント
        if ((i >> j) & 1):  # 順に右にシフトさせ最下位bitのチェックを行う
            bag.append(j)  # フラグが立っていたら bag に果物を詰める
    plus = 0
    minas = 0
    for key,val in enumerate(item):
        if key in bag:
            plus += val
        else:
            minas += val
    if plus == minas:
        print('Yes')
        exit()

print('No')