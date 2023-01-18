import itertools


def solution(l):
    permutations = itertools.chain.from_iterable(
        itertools.permutations(l, n) for n in range(len(l), 0, -1)
    )
    max_num = 0

    for perm in permutations:
        num = int("".join(map(str, perm)))

        if num % 3 == 0:
            max_num = max(max_num, num)

    return max_num


print "([1]): expected=0 actual={}".format(solution([1]))
print "([3]): expected=3 actual={}".format(solution([3]))
print "([3, 1, 4, 1]): expected=4311, actual={}".format(solution([3, 1, 4, 1]))
print "([3, 1, 4, 1, 5, 9]): expected=94311, actual={}".format(solution([3, 1, 4, 1, 5, 9]))
