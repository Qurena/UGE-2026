

import sys
sys.setrecursionlimit(5000)
def count(start, end, cmd_count):
    if start == end and cmd_count <= 15: # УСЛОВИЕ ПОБЕДЫ
        return 1

    if cmd_count > 15: # УСЛОВИЕ ПОРАЖЕНИЯ
        return 0

    if start == 27: # УСЛОВИЕ ПОРАЖЕНИЯ
        return 0

    if start > end: # УСЛОВИЕ ПОРАЖЕНИЯ
        return 0

    return (count(start + 2, end, cmd_count + 1) + # УСЛОВИЕ ДЕЙСТВИЙ
            count(start * 3, end, cmd_count + 1) +
            count(start ** 3, end, cmd_count + 1)
            )


print(count(3, 125, 0))
# 12
