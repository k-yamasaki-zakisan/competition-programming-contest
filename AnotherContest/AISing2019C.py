# https://atcoder.jp/contests/aising2019/tasks/aising2019_c

H,W = map(int,input().split())
S = [list(input()) for _ in range(H)]
check = [[0]*W for _ in range(H)]
ans = 0
for h in range(H):
    for w in range(W):
        if check[h][w] == 1:
            continue
        black, white = 0, 0

        stack = [[h,w]]
        check[h][w] = 1
        if S[h][w] == '#':
            black += 1
        elif S[h][w] == '.':
            white += 1
        
        while len(stack):
            y,x = stack.pop()
            tmp = S[y][x]
            for dy,dx in [[1,0],[-1,0],[0,1],[0,-1]]:
                ny,nx = y+dy,x+dx
                if 0 <= ny < H and 0 <= nx < W and tmp != S[ny][nx] and check[ny][nx] == 0:
                    check[ny][nx] = 1
                    stack.append([ny,nx])
                    if S[ny][nx] == '#':
                        black += 1
                    elif S[ny][nx] == '.':
                        white += 1
        ans += black*white
print(ans)