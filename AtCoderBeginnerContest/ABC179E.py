#https://atcoder.jp/contests/abc179/tasks/abc179_e

N,X,M = map(int,input().split())
#全体ループを見る配列
t_loop = [X]
#初回ループを見る配列
f_loop = [X]
#出現回数を見る辞書
memo = {X:1}
#2回目以降のループを見る配列
s_loop = []
while True:
    new_val = t_loop[-1]**2%M
    t_loop.append(new_val)
    if new_val not in memo:
        memo[new_val] = 1
        f_loop.append(new_val)
    else:
        memo[new_val] += 1
        if memo[new_val] == 3:
            break
        else:
            s_loop.append(new_val)

ans = 0
if N <= len(f_loop):
    ans += sum(f_loop[:N])
else:
    ans += sum(f_loop)
    shou = (N-len(f_loop))//len(s_loop)
    amari = (N-len(f_loop))%len(s_loop)
    ans += shou*sum(s_loop)
    ans += sum(s_loop[:amari])
    
print(ans)
