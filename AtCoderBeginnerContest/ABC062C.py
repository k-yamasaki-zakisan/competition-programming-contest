#https://atcoder.jp/contests/abc062/tasks/arc074_a

h,w = map(int,input().split())

ans = float('inf')

if h%3==0 or w%3==0:
    print(0)
    exit()

#縦割り
ans = min(ans, w)

#横割り
ans = min(ans, h)

#縦割り+横半分
for x in range(1, w+1):
    tate_area = x*h
    yoko_min_area = (w-x)*(h//2)
    yoko_max_area = (w-x)*(h-h//2)
    area_max = max(tate_area, yoko_min_area, yoko_max_area)
    area_min = min(tate_area, yoko_min_area, yoko_max_area)
    ans = min(ans, area_max-area_min)
    #print(ans, tate_area, yoko_min_area, yoko_max_area)

#横割り+縦半分
for y in range(h//3, h+1):
    yoko_area = y*w
    tate_min_area = (h-y)*(w//2)
    tate_max_area = (h-y)*(w-w//2)
    area_max = max(yoko_area, tate_min_area, tate_max_area)
    area_min = min(yoko_area, tate_min_area, tate_max_area)
    ans = min(ans, area_max-area_min)

print(ans)
