#https://atcoder.jp/contests/agc034/tasks/agc034_b

S = input()
ans = 0
idx = 0
a_count = 0
while idx < len(S):
    if S[idx] == "A":
        a_count += 1
    elif S[idx:idx+2] == "BC":
        ans += a_count
        idx += 1
    else:
        a_count = 0
    idx += 1
print(ans)
