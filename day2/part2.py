from grab_input import grab_input

grab_input("https://adventofcode.com/2025/day/2/input")


def get_splits(length):
    possible = []
    for pl in range(1, length // 2 + 1):
        if length % pl == 0:
            rep = length // pl
            possible.append((pl, rep))
    return possible


def main():
    invalid_ids = 0
    with open("input.txt", "r") as f:
        for range_ in f.readline().split(","):
            firstNum, secondNum = range_.split("-")
            fint, sint = int(firstNum), int(secondNum)

            for i in range(fint, sint + 1):
                si = str(i)
                splits = get_splits(len(si))

                for pattern_length, repeating in splits:
                    first_chunk = si[0:pattern_length]

                    if first_chunk * repeating == si:
                        invalid_ids += int(i)
                        break

    return invalid_ids


if __name__ == "__main__":
    print(main())
