from collections.abc import Iterable


def solve(lines: Iterable[str]) -> int:
    left = []
    right = {}

    for line in lines:
        [l, r] = line.split()

        left.append(l)

        curr = right.get(r) or 0
        right[r] = curr + 1

    sum = 0

    for el in left:
        count = right.get(el) or 0
        sum += int(el) * count

    return sum
