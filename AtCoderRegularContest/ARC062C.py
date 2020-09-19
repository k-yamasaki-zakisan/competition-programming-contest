#https://atcoder.jp/contests/arc062/submissions/16831794

N = int(input())

t_cunt = a_cunt = 1

for _ in range(N):
    T,A = map(int,input().split())
    if T < t_cunt or A < a_cunt:
        nt = t_cunt//T + 1 if t_cunt%T else t_cunt//T
        na = a_cunt//A + 1 if a_cunt%A else a_cunt//A
        n = max(nt, na)
        t_cunt = n*T
        a_cunt = n*A
    else:
        t_cunt = T
        a_cunt = A
    #print(t_cunt, a_cunt)
print(t_cunt+a_cunt)
