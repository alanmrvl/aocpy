from collections.abc import Iterable


def solve(lines: Iterable[str]) -> int:
    count = 0

    input = lines.readline()

    ranges = list(map(lambda x: list(map(int, x.split("-"))), input.split(",")))

    for [start, end] in ranges:
        for n in range(start, end + 1):
            ns = str(n)

            if len(ns) % 2 != 0:
                continue

            mid = len(ns) // 2

            if ns[:mid] == ns[mid:]:
                count += n
                print(ns)

    print()

    return count
