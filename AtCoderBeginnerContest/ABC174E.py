#https://atcoder.jp/contests/abc174/tasks/abc174_e

n,k = map(int,input().split())

a = list(map(int,input().split()))

a.sort()

max_tree = max(a)

min_tree = 0

while min_tree+1 != max_tree:
    mid_tree = (max_tree+min_tree)//2
    tmp_count = 0
    for i in range(n-1,-1,-1):
        if a[i] < mid_tree:
            break
        
        if a[i]%mid_tree == 0:
            tmp_count += a[i]//mid_tree-1
        else:
            tmp_count += a[i]//mid_tree

    if k < tmp_count:
        min_tree = mid_tree
    else:
        max_tree = mid_tree
    #print(max_tree, min_tree,tmp_count)
print(max_tree)
