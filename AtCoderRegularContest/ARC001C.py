# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_13_A&lang=ja
# https://kakedashi-engineer.appspot.com/2020/05/09/alds1-13a/

from itertools import permutations
N = 8
RC = []
for n in range(N):
    S = list(input())
    for i,s in enumerate(S):
        if s=='Q':
            RC.append((n,i))

# 斜めの判定
def diag(board:list) -> bool: 
    for i in range(2*N-1):
        sm = 0
        for j in range(i+1):
            if 8<=i-j or 8<=j:
                continue
            sm += board[i-j][j]
        if 1<sm:
            return False
    return True

def judge(ls:tuple) -> bool:
    board = [[0]*N for _ in range(N)]
    for r in range(N):
        c = ls[r]
        board[r][c] = 1
    for r,c in RC:  # 指定された箇所にクイーンを置いているか判定
        if board[r][c] == 0:
            return False
    
    if not diag(board):
        return False
    
    if not diag(board[::-1]):  # 反転した結果も判定
        return False

    return True

for ls in permutations(range(N)):
    if judge(ls):
        for c in ls:
            s = ['.'] * N
            s[c] = 'Q'
            print (''.join(s))
        exit()

print('No Answer')