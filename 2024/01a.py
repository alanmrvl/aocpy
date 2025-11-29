from collections.abc import Iterable


def solve(lines: Iterable[str]) -> int:
    left = []
    right = []

    for line in lines:
        [l, r] = line.split()
        left.append(int(l))
        right.append(int(r))

    left.sort()
    right.sort()

    sum = 0

    for i in range(0, len(left)):
        sum += abs(left[i] - right[i])

    return sum
