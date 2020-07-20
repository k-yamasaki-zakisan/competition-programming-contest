#https://atcoder.jp/contests/abc039/tasks/abc039_d

move = [[-1,-1],[-1,0],[0,-1],[0,1],[1,0],[1,1],[1,-1],[-1,1]]

h,w = map(int,input().split())
image = []
for _ in range(h):
    s = list(input())
    image.append(s)

original_image = [[] for _ in range(h)]

visite_black = [[False for i in range(w)] for j in range(h)] 

for i in range(h):
    for j in range(w):
        if image[i][j] == '#':
            flag_block = True
            for x, y in move:
                if -1 < i+y < h and -1 < j+x < w:
                    if image[i+y][j+x] == '.':
                        flag_block = False
                        break
            if flag_block:
                original_image[i].append('#')
                visite_black[i][j] = True
                for x, y in move:
                    if -1 < i+y < h and -1 < j+x < w:
                        visite_black[i+y][j+x] = True 
            else:
                original_image[i].append('.')
        else:
            original_image[i].append('.')

flag_same = True
for i in range(h):
    for j in range(w):
        if image[i][j] == '#' and visite_black[i][j] == False:
            flag_same = False
            break
#print(visite_black)
#print(original_image)
if flag_same:
    print('possible')
    for i in range(h):
        print(''.join(map(str,original_image[i])))
else:
    print('impossible')
