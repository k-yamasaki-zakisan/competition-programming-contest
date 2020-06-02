#https://atcoder.jp/contests/abc169/tasks/abc169_e

N = int(input())
A = [0]*N
B = [0]*N
for i in range(N):
  A[i],B[i] = map(int, input().split())
A.sort()
B.sort(reverse=True)
if N%2==1:
  mid = (N+1)//2-1
  ans = B[mid]-A[mid]+1
else:
  mid1 = N//2-1
  mid2 = N//2
  ans = (B[mid1]+B[mid2])-(A[mid1]+A[mid2])+1

print(ans)
