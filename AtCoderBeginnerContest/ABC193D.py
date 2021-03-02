# https://atcoder.jp/contests/abc193/tasks/abc193_d

K = int(input())
S = input()
T = input()

S = S[:-1]
T = T[:-1]

s_memo = [0]*10
t_memo = [0]*10

cards = [K]*10

s_point = 0
t_point = 0

for s in S:
    s = int(s)
    s_memo[s] += 1
    cards[s] -= 1

for t in T:
    t = int(t)
    t_memo[t] += 1
    cards[t] -= 1

for i in range(1, 10):
    s_point += i*10**s_memo[i]
    t_point += i*10**t_memo[i]

for i in range(1, 10):
    if cards[i] != 0:
        left = i
        break
for i in range(9, 0, -1):
    if cards[i] != 0:
        right = i
        break

hasi_t_point = t_point-right*10**(t_memo[right])+right*10**(t_memo[right]+1)
hasi_s_point = s_point-left*10**(s_memo[left])+left*10**(s_memo[left]+1)
if hasi_t_point < hasi_s_point:
    print(1.0)
    exit()

ans = 0
for s_i in range(1, 10):
    if cards[s_i] == 0:
        continue
    cards[s_i] -= 1
    for t_i in range(1, 10):
        if cards[t_i] == 0:
            continue
        now_t_point = t_point-t_i*10**(t_memo[t_i])+t_i*10**(t_memo[t_i]+1)
        now_s_point = s_point-s_i*10**(s_memo[s_i])+s_i*10**(s_memo[s_i]+1)
        if now_t_point < now_s_point:
            ans += (cards[s_i]+1)*cards[t_i]
    cards[s_i] += 1

N = 9 * K - 8
print(ans / N / (N - 1))
