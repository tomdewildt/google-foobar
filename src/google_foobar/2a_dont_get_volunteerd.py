XM = [2, 1, -1, -2, -2, -1, 1, 2]
YM = [1, 2, 2, 1, -1, -2, -2, -1]


def find_indices(pos):
    return pos % 8, pos // 8


def find_moves(x, y):
    m = []

    for idx in range(8):
        xn = x + XM[idx]
        yn = y + YM[idx]

        if xn >= 0 and yn >= 0 and xn < 8 and yn < 8:
            m.append((xn, yn))

    return m


def solution(src, dest):
    if src == dest:
        return 0

    sx, sy = find_indices(src)
    dx, dy = find_indices(dest)
    queue = []
    queue.extend(find_moves(sx, sy))
    explored = [(sx, sy)]

    depth = 1

    while len(queue) > 0:
        sub_queue = queue[:]

        for x, y in sub_queue:
            if x == dx and y == dy:
                return depth
            if (x, y) in explored:
                continue

            queue.extend(find_moves(x, y))
            explored.append((x, y))

        depth += 1


print "(0, 1): expected=3, actual={}".format(solution(0, 1))
print "(19, 36): expected=1, actual={}".format(solution(19, 36))
