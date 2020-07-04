#https://atcoder.jp/contests/abc138/tasks/abc138_e

#case1

from bisect import bisect_left

s = list(input())

t = list(input())

alf=[[] for _ in range(26)]

for i in range(len(s)):
    alf[ord(s[i])-97].append(i)

now_alf = -1
sets = 0
i = 0

while i < len(t):
    next_alf = ord(t[i])-97

    if len(alf[next_alf]) == 0:
        print(-1)
        exit()

    if now_alf > alf[next_alf][-1]:
        now_alf = -1
        sets += 1
    else:
        serch_next_alf = bisect_left(alf[next_alf], now_alf)
        now_alf = alf[next_alf][serch_next_alf]+1
        i += 1

print(sets*len(s)+now_alf)

#case2
from bisect import bisect_left

s = list(input())

total_s = len(s)

t = list(input())

alf=[[] for _ in range(26)]

for i in range(len(s)):
    alf[ord(s[i])-97].append(i+1)

now_alf = 0
ans = 0

for i in range(len(t)):
    next_alf = ord(t[i])-97

    if len(alf[next_alf]) == 0:
        print(-1)
        exit()

    if 0 < i and t[i-1] == t[i]:
        now_alf += 1
        ans += 1
        if now_alf == total_s and t[i] == s[now_alf-1]:
            continue

    serch_next_alf = bisect_left(alf[next_alf], now_alf)

    if now_alf < alf[next_alf][-1]:
        ans += alf[next_alf][serch_next_alf] - now_alf
        now_alf = alf[next_alf][serch_next_alf]
    else:
        ans += total_s - now_alf + alf[next_alf][0]
        now_alf = alf[next_alf][0]

print(ans)

