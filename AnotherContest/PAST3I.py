# https://atcoder.jp/contests/past202005-open/tasks/past202005_i

N = int(input())
Q = int(input())
Query = [list(map(int,input().split())) for _ in range(Q)]
X = [a for a in range(N)]
Y = [a for a in range(N)]
Trans = False
for k in range(Q):
    if Query[k][0] == 3:
        Trans = not Trans
        X,Y = Y,X
    else:
        A,B = Query[k][1]-1, Query[k][2]-1
        if Query[k][0] == 1:
            X[A],X[B] = X[B],X[A]
        elif Query[k][0] == 2:
            Y[A],Y[B] = Y[B],Y[A]
        else:
            i,j = X[A],Y[B]
            if Trans:  
                print(j*N+i)
            else:
                print(i*N+j)