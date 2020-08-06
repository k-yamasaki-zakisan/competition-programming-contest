#https://atcoder.jp/contests/abc170/tasks/abc170_e

from heapq import heappop, heappush

n,Q = map(int,input().split())
M =2*(10**5)

belong = [0] * n  # 幼児iの所属先の幼稚園
rate = [0] * n  # 幼児iのレート
kindergarten = [[] for _ in range(M+1)] # 幼稚園キュー. (レート[降順], 幼児)

for c in range(n):
    a,b = map(int,input().split())
    b -= 1
    heappush(kindergarten[b],(-a,c))
    belong[c] = b
    rate[c] = a

q = []  # 最強園児の順序付きキュー.(レート[昇順], 幼児, 園)
for i in range(M):
    if kindergarten[i]:
        a,c = kindergarten[i][0]
        heappush(q,(-a,c,i))

for s in range(Q):
    C, D = map(int,input().split())
    C, D = C-1, D-1

    pd = belong[C] # 移動元の幼稚園
    belong[C] = D  # 当該幼児のbelongを更新

    # 移動元の幼稚園キューを更新
    while kindergarten[pd]:
        A, c = kindergarten[pd][0]
        # キューの先頭の幼児が既に存在しないとき取り除く.
        # 存在するとき, 最強幼児キューへ追加.
        if belong[c] != pd:
            heappop(kindergarten[pd])
        else:
            heappush(q, (-A, c, pd))
            break

    heappush(kindergarten[D], (-rate[C], C))

    while kindergarten[D]:
        A, c = kindergarten[D][0]
        # キューの先頭の幼児が既に存在しないとき取り除く.
        # 存在するとき, 最強幼児キューへ追加.
        if belong[c] != D:
            heappop(kindergarten[D])
        else:
            heappush(q, (-A, c, D))
            break

    while q:
        A, c, d = q[0]
        # キューの先頭の幼児が既に去っている or 所属する幼稚園キューの先頭では無い とき取り除く.
        # そうではないとき、これが答えとなるためprintする.
        if belong[c] != d or kindergarten[d][0][1] != c:
            heappop(q)
        else:
            print(A)
            break
