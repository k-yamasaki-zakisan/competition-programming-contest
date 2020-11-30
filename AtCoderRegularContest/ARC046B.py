# https://atcoder.jp/contests/arc046/tasks/arc046_b

N = int(input())
A,B = map(int,input().split())
if A == B:
    if A+1 == N:
        print('Aoki')
    elif N%(A+1) == 0:
        print('Aoki')
    else:
        print('Takahashi')
else:
    if N <= A:
        print('Takahashi')
    elif B < A:
        print('Takahashi')
    else:
        print('Aoki')