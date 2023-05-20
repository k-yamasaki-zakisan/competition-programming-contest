def count_by_date(space_id: int, day: int, ks: list) -> None:
    create_ks_count = [0] * (day + 1)
    delete_ks_count = [0] * (day + 1)
    for id, create_day, delete_day in ks:
        if id != space_id:
            continue
        create_ks_count[create_day] += 1
        if delete_day is not None:
            delete_ks_count[delete_day] += 1

    ks_day_count = []
    now_count = 0
    for i in range(day + 1):
        now_count += create_ks_count[i]
        now_count -= delete_ks_count[i]
        ks_day_count.append(now_count)

    for count in ks_day_count:
        print(count)
    return ks_day_count


# space_id = 0
# day = 3
# ks = [
#     [0, 0, 3],
#     [0, 1, None],
#     [0, 3, None],
#     [1, 0, None],
# ]
# countByDate(space_id, )
