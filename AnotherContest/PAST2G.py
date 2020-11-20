#https://atcoder.jp/contests/past202004-open/tasks/past202004_g

from collections import deque

q=int(input())

memo = deque()

for _ in range(q):
    ans = 0
    query = input().split()
    if query[0] == '1':
      memo.append([query[1] , int(query[2])])
    else:
      memo_erase = {}
      erase_count = int(query[1])
      while erase_count > 0 and len(memo) > 0:
        if memo[0][1] <= erase_count:
          erase_count -= memo[0][1]
          alf , moji_su = memo.popleft()
          if alf in memo_erase:
            memo_erase[alf] += moji_su
          else:
            memo_erase[alf] = moji_su
        else:
          memo[0][1] -= erase_count
          if memo[0][0] in memo_erase:
            memo_erase[memo[0][0]] += erase_count
          else:
            memo_erase[memo[0][0]] = erase_count
          erase_count = 0

      for v in memo_erase.values():
        ans += v**2
      print(ans)



# 別解
# from collections import deque
# N = int(input())
# Query = [list(map(str,input().split())) for _ in range(N)]

# moji = deque([])
# for i in range(N):
#     if Query[i][0] == '1':
#         alf,q = Query[i][1],int(Query[i][2])
#         moji.append([alf,q])
#     else:
#         ans = {}
#         rm_cnt = int(Query[i][1])
#         if len(moji) and rm_cnt < moji[0][1]:
#             ans[moji[0][0]] = rm_cnt
#             moji[0][1] -= rm_cnt
#         else:
#             while len(moji) and moji[0][1] <= rm_cnt:
#                 rm_cnt -= moji[0][1]
#                 if moji[0][0] in ans:
#                     ans[moji[0][0]] += moji[0][1]
#                 else:
#                     ans[moji[0][0]] = moji[0][1]
#                 moji.popleft()
#             if len(moji) and rm_cnt < moji[0][1]:
#                 if moji[0][0] in ans:
#                     ans[moji[0][0]] += rm_cnt
#                 else:
#                     ans[moji[0][0]] = rm_cnt
#                 moji[0][1] -= rm_cnt
#         print(sum(i**2 for i in ans.values()))
