#https://atcoder.jp/contests/arc014/tasks/arc014_3

n=int(input())

s=list(input())

r = 0

b = 0

g = 0
#色別に数を数えて、奇数種類の合計値
for i,color in enumerate(s):
    if color == 'R':
        r += 1
    elif color == 'G':
        g += 1
    else:
        b += 1

print(r%2+g%2+b%2)
