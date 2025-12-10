from grab_input import grab_input

grab_input("https://adventofcode.com/2025/day/3/input")


def main():
    max_num = 0
    total = 0

    with open("input.txt", "r") as f:
        for line in f.readlines():
            line = line.strip()
            max_num = 0

            for idx, i in enumerate(line):
                for j in line[idx + 1 :]:
                    num = int(i + j)

                    if num > max_num:
                        max_num = num

            total += max_num

    return total


if __name__ == "__main__":
    print(main())
