# https://atcoder.jp/contests/past202012-open/tasks/past202012_h

from collections import deque

H, W = map(int, input().split())
r, c = map(int, input().split())
r, c = r-1, c-1
S = [list(input()) for _ in range(H)]
stack = deque([[r, c]])
ans = [['.']*W for _ in range(H)]
ans[r][c] = 'o'
for h in range(H):
    for w in range(W):
        if S[h][w] == '#':
            ans[h][w] = '#'
while len(stack):
    h, w = stack.popleft()
    for ny, nx in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
        y, x = h+ny, w+nx
        if 0 <= y < H and 0 <= x < W and ans[y][x] == '.':
            if (S[y][x] == '.') or (S[y][x] == '^' and ny == 1 and nx == 0) or (S[y][x] == 'v' and ny == -1 and nx == 0) or (S[y][x] == '<' and ny == 0 and nx == 1) or (S[y][x] == '>' and ny == 0 and nx == -1):
                stack.append([y, x])
                ans[y][x] = 'o'
for a in ans:
    tmp = ''.join(map(str, a))
    tmp = tmp.replace('.', 'x')
    print(tmp)
