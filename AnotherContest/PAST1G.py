# https://atcoder.jp/contests/past201912-open/tasks/past201912_g

from itertools import combinations

N = int(input())
happy_cost = [[0]*N for _ in range(N)]
ans = 0
for i in range(N-1):
    A = list(map(int,input().split()))
    ans += sum(A)
    j = i+1
    for a in A:
        happy_cost[i][j] = a
        j += 1

cnd = [i for i in range(N)]
# 2チーム
for i in range(1,N):
    for f_team in combinations(cnd,i):
        tmp = 0
        s_team = []
        #セカンドチーム作成
        for c in cnd:
            if c not in f_team:
                s_team.append(c)
        for i in range(len(f_team)-1):
            for j in range(i+1, len(f_team)):
                tmp += happy_cost[f_team[i]][f_team[j]]
        for i in range(1,len(s_team)-1):
            for j in range(i+1, len(s_team)):
                tmp += happy_cost[s_team[i]][s_team[j]]
        ans = max(ans, tmp)

# 3チーム
for i in range(1,N-1):
    for f_team in combinations(cnd,i):
        except_team = []   
        for c in cnd:
            if c not in f_team:
                except_team.append(c)
        #セカンドチーム作成
        for j in range(1,N-i+1):
            for s_team in combinations(except_team,j):
                t_team = []
                tmp = 0
                # サードチーム作成
                for c in cnd:
                    if c not in f_team and c not in s_team:
                        t_team.append(c)
                for i in range(len(f_team)-1):
                    for j in range(i+1, len(f_team)):
                        tmp += happy_cost[f_team[i]][f_team[j]]
                for i in range(len(s_team)-1):
                    for j in range(i+1, len(s_team)):
                        tmp += happy_cost[s_team[i]][s_team[j]]
                for i in range(len(t_team)-1):
                    for j in range(i+1, len(t_team)):
                        tmp += happy_cost[t_team[i]][t_team[j]]
                ans = max(ans,tmp)
print(ans)