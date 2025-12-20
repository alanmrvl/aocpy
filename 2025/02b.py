from collections.abc import Iterable


def solve(lines: Iterable[str]) -> int:
    count = 0

    input = lines.readline()

    ranges = list(map(lambda x: list(map(int, x.split("-"))), input.split(",")))

    for [start, end] in ranges:
        for n in range(start, end + 1):
            ns = str(n)

            if len(ns) > 1 and len(set(ns)) == 1:
                print(str(n))
                count += n
                continue

            found = False
            for i in range(2, len(ns)):
                if found:
                    break

                if len(ns) % i == 0:
                    chunks = [ns[j : j + i] for j in range(0, len(ns), i)]
                    if len(set(chunks)) == 1:
                        print(str(n) + " " + str(i) + " " + str(chunks))
                        count += n
                        found = True

    print()

    return count
