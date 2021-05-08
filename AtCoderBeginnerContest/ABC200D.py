# https://atcoder.jp/contests/abc200/tasks/abc200_d

N = int(input())
A = list(map(int, input().split()))
mod200 = [0]*200

for i in range(2**N):
    s = 0
    l = []
    for j in range(N):
        if i & (1 << j):
            s += A[j]
            l.append(j+1)
    s %= 200
    if mod200[s]:
        print('Yes')
        print(*([len(l)]+l))
        print(*([len(mod200[s])]+mod200[s]))
        exit()
    mod200[s] = l
print('No')

# 別解

# def output(b_key: int, c_list: list):
#     print('Yes')
#     print(len(dp[b_key]), *dp[b_key])
#     print(len(c_list), *c_list)
#     exit()


# N = int(input())
# A = list(map(int, input().split()))
# A_amari = [a % 200 for a in A]
# dp = {}
# for i, a in enumerate(A_amari):
#     if a in dp:
#         output(a, [i+1])
#     d = {}
#     for key, val in dp.items():
#         nv = (key+a) % 200
#         if nv in dp:
#             output(nv, val+[i+1])
#         d[nv] = val+[i+1]
#     d[a] = [i+1]
#     dp = {**dp, **d}
# print('No')
