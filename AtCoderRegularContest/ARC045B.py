# https://atcoder.jp/contests/arc045/tasks/arc045_b

N, M = map(int, input().split())
ST = [list(map(int, input().split())) for _ in range(M)]
room = [0]*(N+2)
for s, t in ST:
    room[s] += 1
    room[t+1] -= 1
for i in range(1, len(room)):
    room[i] += room[i-1]

ruiseki_room = [0]*(N+2)
for i in range(len(room)):
    if room[i] == 1:
        ruiseki_room[i] = 1

for i in range(1, len(ruiseki_room)):
    ruiseki_room[i] += ruiseki_room[i-1]

ans = []
for i, st in enumerate(ST):
    s, t = st
    if ruiseki_room[t]-ruiseki_room[s-1] == 0:
        ans.append(i+1)
print(len(ans))
for a in ans:
    print(a)
