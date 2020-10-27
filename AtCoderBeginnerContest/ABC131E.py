# https://atcoder.jp/contests/abc131/tasks/abc131_e
# スターグラフを作成後、端の点を繋げて任意数の最短距離2グラフを作成

N,K = map(int,input().split())

dist_2 = (N-1)*(N-2)//2

if dist_2 < K:
    print(-1)
    exit()

# スターグラフ作成
root = [[1,i] for i in range(2,N+1)]

# 葉を繋げて最短距離2である数を削る
for i in range(2,N):
    for j in range(i+1,N+1):
        if dist_2 == K:
            break
        root.append([i,j])
        dist_2 -= 1

print(len(root))
for a,b in root:
    print(a,b)