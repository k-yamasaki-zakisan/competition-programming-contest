# https://atcoder.jp/contests/abc082/tasks/arc087_b

S = input().split('T')
X, Y = map(int, input().split())
now_posi_x = set([len(S.pop(0))])
now_posi_y = set([0])
dx = []
dy = []
for i, s in enumerate(S):
    if i % 2:
        dx.append(len(s))
    else:
        dy.append(len(s))

for x in dx:
    tmp_move = set()
    for position in now_posi_x:
        tmp_move.add(position+x)
        tmp_move.add(position-x)
    now_posi_x = tmp_move

for y in dy:
    tmp_move = set()
    for position in now_posi_y:
        tmp_move.add(position+y)
        tmp_move.add(position-y)
    now_posi_y = tmp_move

if X in now_posi_x and Y in now_posi_y:
    print('Yes')
else:
    print('No')
