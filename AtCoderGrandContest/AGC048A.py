# https://atcoder.jp/contests/agc048/tasks/agc048_a

act = 'atcoder'

T = int(input())

for _ in range(T):
    S = input()
    if act < S:
        print(0)
        continue
    S = list(S)
    SC = sorted(S)
    SC = SC[::-1]
    if ''.join(SC) < act:
        print(-1)
        continue
    ans = 0
    for i in range(len(S)):
        if 'a' != S[i]:
            if 't' < S[i]:
                print(i-1)
            else:
                print(i)
            break