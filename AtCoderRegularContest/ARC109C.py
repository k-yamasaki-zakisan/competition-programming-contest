# https://atcoder.jp/contests/arc109/tasks/arc109_c

n, k = map(int, input().split())
s = input()
 
res = {
    ('R', 'S'):'R',
    ('S', 'R'):'R',
    ('R', 'P'):'P',
    ('P', 'R'):'P',
    ('P', 'S'):'S',
    ('S', 'P'):'S',
    ('S', 'S'):'S',
    ('P', 'P'):'P',
    ('R', 'R'):'R'
}
 
cur = list(s)
for _ in range(k):
    cur = cur + cur
    temp = []
    for i in range(len(cur)//2):
        temp.append(res[(cur[2*i], cur[2*i+1])])
    cur = temp
print(cur[0])