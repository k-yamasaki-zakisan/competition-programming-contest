#https://atcoder.jp/contests/past202004-open/tasks/past202004_h

H,W = map(int,input().split())
root = [list(input()) for _ in range(H)]
points = [[] for _ in range(11)]
for h in range(H):
    for w in range(W):
        if root[h][w] == "S":
            points[0].append((h,w))
        elif root[h][w] == "G":
            points[10].append((h,w))
        else:
            points[int(root[h][w])].append((h,w))
dp = [[10**10]*W for _ in range(H)]
start = points[0][0]
dp[start[0]][start[1]] = 0
for i in range(1,11):
    for nh,nw in points[i]:
        for ph,pw in points[i-1]:
            dist = abs(nh-ph)+abs(nw-pw)
            dp[nh][nw] = min(dp[nh][nw], dp[ph][pw]+dist)
goal_h,gool_w = points[10][0]
if dp[goal_h][gool_w] != 10**10:
    print(dp[goal_h][gool_w])
else:
    print(-1)


# 計算量ミスの想定解
# import sys
# input = sys.stdin.readline
# sys.setrecursionlimit(10 ** 7)

# H,W = map(int,input().split())

# nums = {}
# for i in range(1,10):
#     nums[i] = []

# for h in range(H):
#     A = list(input())
#     for w in range(W):
#         if A[w] == 'S':
#             start = [h,w]
#         elif A[w] == 'G':
#             goal = [h,w]
#         else:
#             nums[int(A[w])].append([h,w])

# ans = []
# def dps(ex_position:list,now_num:int,tmp_cnt:int):
#     for h,w in nums[now_num]:
#         next_tmp_cnt = tmp_cnt+abs(h-ex_position[0])+abs(w-ex_position[1])
#         if now_num+1 < 10:
#             dps([h,w], now_num+1, next_tmp_cnt)
#         else:
#             final_cnt = next_tmp_cnt+abs(h-goal[0])+abs(w-goal[1])
#             ans.append(final_cnt)

# dps(start,1,0)

# if len(ans):
#     print(min(ans))
# else:
#     print(-1)