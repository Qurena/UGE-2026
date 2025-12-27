def third_command(key):
    if key % 3 == 0:
        key += 3
    else:
        while key % 3 != 0:
            key += 1
    return int(key)


def count(start: int, end: int) -> int:
    d = {}

    for key in range(start, end + 1):
        d[key] = 0

    d[start] = 1

    if 50 in d:
        del d[50]

    for key in d.keys():
        if key + 3 in d:
            d[key + 3] += d[key]
        if key * 2 + 1 in d:
            d[key * 2 + 1] += d[key]
        if third_command(key) in d:
            d[third_command(key)] += d[key]

    return d[end]

