from grab_input import grab_input
from itertools import combinations

grab_input("https://adventofcode.com/2025/day/3/input")

# This runs extremely slow, but I cant be asked to optimize it


def main():
    max_num = 0
    total = 0

    with open("input.txt", "r") as f:
        for line in f.readlines():
            line = line.strip()
            max_num = 0

            for i in combinations(line, r=12):
                num = int("".join(i))
                if num > max_num:
                    max_num = num

            total += max_num

    return total


if __name__ == "__main__":
    print(main())
