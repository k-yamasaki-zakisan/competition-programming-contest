# https://atcoder.jp/contests/typical90/tasks/typical90_cd

MOD = 10**9+7

L, R = map(int, input().split())
s = len(str(L))
g = len(str(R))
ans = 0
for i in range(s, g+1):
    tmp_s_num = int('1'+'0'*(i-1))
    s_num = max(tmp_s_num, L)
    tmp_g_num = int('9'*i)
    g_num = min(tmp_g_num, R)
    ans += (g_num+s_num)*(g_num-s_num+1)//2*i
    ans %= MOD
print(ans % MOD)
