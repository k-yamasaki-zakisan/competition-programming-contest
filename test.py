def countByDate(spaceID: int, day: int, ks: list) -> list:
    ks_count = [0] * (day + 1)
    for ks_space_id, created_date, deleted_date in ks:
        if spaceID != ks_space_id:
            continue
        ks_count[created_date] += 1
        if deleted_date is not None:
            ks_count[deleted_date] -= 1
    for i in range(1, len(ks_count)):
        ks_count[i] += ks_count[i - 1]
    print(ks_count)

    return ks_count


countByDate(0, 3, [[0, 0, 3], [0, 1, None], [0, 3, None], [1, 0, None]])

# 9779
# 99799
# 999999
# 9994999
# 99944999
# and
for i in range(100000):
    if i % 7 == 0 and str(i)[:2] == str(i)[3:][::-1]:
        print(i)
print(i)
