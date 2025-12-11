from grab_input import grab_input

grab_input("https://adventofcode.com/2025/day/5/input")


def main():
    fresh = 0
    seen = set()

    with open("input.txt", "r") as f:
        ranges, available = f.read().split("\n\n")

        for number in available.splitlines():
            n = int(number)

            if number in seen:
                continue

            for range in ranges.splitlines():
                a, b = range.split("-")
                a, b = int(a), int(b)

                if a <= n <= b:
                    fresh += 1
                    seen.add(number)
                    break

    return fresh


if __name__ == "__main__":
    print(main())
