# https://atcoder.jp/contests/abc141/tasks/abc141_e
# 分割して前の文字列にあうものを後ろの文字列から検索

N = int(input())
S = input()
ans = 0
for i in range(N):
    if N-i<ans:
        continue
    # print(S[i-ans:i+1], S[i+1:])
    if 0<=S[i+1:].find(S[i-ans:i+1]):
        ans += 1
print(ans)

# in
# 13
# strangeorange

# out
# 5

#run time space
# s trangeorange
# t rangeorange
# r angeorange
# ra ngeorange
# ran georange
# rang eorange
# range orange
# rangeo range
# angeor ange
