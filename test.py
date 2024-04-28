test = [(1, 1), (2, 2), (1, 1)]
tmp_i = sorted(test, key=lambda x: -x[1])
print(tmp_i)
print(test[0:])
