from grab_input import grab_input

grab_input("https://adventofcode.com/2025/day/2/input")


def main():
    invalid_ids = 0
    with open("input.txt", "r") as f:
        for range_ in f.readline().split(","):
            firstNum, secondNum = range_.split("-")
            fint, sint = int(firstNum), int(secondNum)

            for i in range(fint, sint + 1):
                si = str(i)

                if len(si) % 2 != 0:
                    # we know its valid since we cant split into two even pieces
                    continue

                first_half = si[0 : len(si) // 2]
                second_half = si[len(si) // 2 : len(si)]

                if first_half == second_half:
                    invalid_ids += int(i)

    return invalid_ids


if __name__ == "__main__":
    print(main())
