from grab_input import grab_input

grab_input("https://adventofcode.com/2025/day/5/input")


def main():
    with open("input.txt", "r") as f:
        ranges, available = f.read().split("\n\n")

        range_list = []
        for range_ in ranges.splitlines():
            a, b = range_.split("-")
            a, b = int(a), int(b)
            range_list.append((a, b))

        range_list.sort()

        merged = []
        for start, end in range_list:
            if merged and start <= merged[-1][1] + 1:
                merged[-1] = (merged[-1][0], max(merged[-1][1], end))
            else:
                merged.append((start, end))

        count = 0
        for start, end in merged:
            count += end - start + 1

    return count


if __name__ == "__main__":
    print(main())
