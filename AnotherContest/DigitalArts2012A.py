#https://atcoder.jp/contests/digitalarts2012/tasks/digitalarts_1

S = list(map(str,input().split()))
N = int(input())
NG = {}
for i in range(N):
    t = input()
    if len(t) in NG:
        NG[len(t)].append(t)
    else:
        NG[len(t)] = [t]
ans = []
for s in S:
    if len(s) not in NG:
        ans.append(s)
    else:
        ngFlag = False
        for ng in NG[len(s)]:
            tmpFlag = True
            for i in range(len(s)):
                if ng[i] == '*' or ng[i] == s[i]:
                    continue
                else:
                    tmpFlag = False
                    break
            if tmpFlag:
                ngFlag = True
                break
        if ngFlag:
            ans.append('*'*len(s))
        else:
            ans.append(s)
print(*ans)
