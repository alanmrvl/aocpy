from collections.abc import Iterable


def solve(lines: Iterable[str]) -> int:
    pos = 50
    count = 0
    max_size = 100

    print("<<start>>: " + str(pos))

    for line in lines:
        print()

        dir = line[0:1]
        dist = int(line[1:])

        raw_pos = (pos - dist) if dir == "L" else (pos + dist)

        new_pos = raw_pos % max_size
        rounds = abs(raw_pos // max_size)

        print("raw_pos: " + str(raw_pos))
        print("new_pos: " + str(new_pos))

        if raw_pos == 0:
            rounds += 1

        if pos == 0 and raw_pos < 0:
            rounds -= 1

        if raw_pos < 0 and raw_pos % 100 == 0:
            rounds += 1

        if rounds > 0:
            count += rounds
            print("ROUND adding: " + str(rounds))

        pos = new_pos

        print(line[:-1] + ": " + str(pos) + " " + str(count))

    return count
