from grab_input import grab_input

grab_input("https://adventofcode.com/2025/day/1/input")


def main():
    starting_point = 50
    ends_0 = 0

    # I honestly think there is something better to use here but I am not sure
    direction = {"R": int.__add__, "L": int.__sub__}

    with open("input.txt", "r") as f:
        for line in f.readlines():
            move_by = int(line[1:-1])

            # Use modulous to handle the wrapping
            # Remainder is the wrapped value, 115 % 100 = 1 R 15 so 15 is the value
            starting_point = direction[line[0]](starting_point, move_by) % 100

            if starting_point == 0:
                ends_0 += 1

    return ends_0


print(main())
