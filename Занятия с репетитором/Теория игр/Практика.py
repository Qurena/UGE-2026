"""ДЗ по номерам 19-21"""
# 19-21
'''https://kompege.ru/task №4379'''

def steps(p):
    next_steps = [p + 1, p + 2, p * 2]
    return next_steps

def play(p, r):
    if p >= 51 and r in (0, 2):
        return True

    if p >= 51 or r == 0:
        return False

    next_plays = [play(step, r - 1) for step in steps(p)]

    return any(next_plays) if r % 2 != 0 else all(next_plays)

for s in range(1, 51):
    if play(s, 1):
        print(s)

