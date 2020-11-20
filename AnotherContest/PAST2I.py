# https://atcoder.jp/contests/past202004-open/tasks/past202004_i

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

N = int(input())
A = list(map(int,input().split()))
fighters = [[i,a] for i,a in enumerate(A)]
battle_cnt = 1
ans = [-1]*(2**N)

def battle(exit_fighters:list, battle_cnt:int) -> list:
    winners = []
    for i in range(1,len(exit_fighters),2):
        if exit_fighters[i-1][1] < exit_fighters[i][1]:
            winners.append(exit_fighters[i])
            ans[exit_fighters[i-1][0]] = battle_cnt
        else:
            winners.append(exit_fighters[i-1])
            ans[exit_fighters[i][0]] = battle_cnt
    if len(winners):
        battle(winners, battle_cnt+1)

battle(fighters, battle_cnt)

max_battle_cnt = max(ans)
for a in ans:
    if 0<a:
        print(a)
    else:
        print(max_battle_cnt)