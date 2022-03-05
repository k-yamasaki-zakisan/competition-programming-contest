a = "ababa"
print(a[0:1])
print(a[1:])
print(a[:-1])
memo = [1]
for _ in range(63):
    memo.append(memo[-1] * 2)
print(*memo)
