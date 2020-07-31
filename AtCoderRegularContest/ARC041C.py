#https://atcoder.jp/contests/arc041/tasks/arc041_c

def block_max_count(right, left):
    right_count = len(right)
    left_count = len(left)
    right_sum = sum(right)
    left_sum = sum(left)
    step = 0
    if right_count == 0:
        rp, lp = 0, 1
    elif left_count == 0:
        rp, lp = l, l+1
    else:
        if left_count < right_count:
            rp ,lp = left[0]-1 , left[0]
        else:
            rp ,lp = right[-1] , right[-1]+1
    right.reverse()
    for j in right:
        step += rp - j
        rp -= 1
    for j in left:
        step += j - lp
        lp += 1
        
    return step


n,l = map(int,input().split())

right = [] 
left = []
block_check = 'R'
ans = 0

for i in range(n):
    x,d = map(str,input().split())
    x = int(x)
    if d == 'R' and block_check == 'R':
        right.append(x)
    elif d == 'R' and block_check == 'L':
        ans += block_max_count(right, left)
        right = [x]
        left = []
        block_check = 'R'
    elif d == 'L':
        left.append(x)
        block_check = 'L'

ans += block_max_count(right, left)

print(ans)
