from collections.abc import Iterable


def solve(lines: Iterable[str]) -> int:
    pos = 50
    count = 0
    max_size = 100

    print("<<start>>: " + str(pos))

    for line in lines:
        dir = line[0:1]
        dist = int(line[1:])

        if dir == "L":
            pos = (pos - dist) % max_size
        else:
            pos = (pos + dist) % max_size

        if pos == 0:
            count += 1

        print(line[:-1] + ": " + str(pos))

    return count
