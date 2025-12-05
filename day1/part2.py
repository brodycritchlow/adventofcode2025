from grab_input import grab_input

grab_input("https://adventofcode.com/2025/day/1/input")


def main():
    starting_point = 50
    crossed_0 = 0

    with open("input.txt", "r") as f:
        for line in f.readlines():
            move_by = int(line[1:-1])

            if line[0] == "R":
                crossings = (starting_point + move_by) // 100
                starting_point = (starting_point + move_by) % 100
            else:
                if starting_point == 0:
                    crossings = move_by // 100
                elif move_by >= starting_point:
                    # count first crossing, plus check if we cross 100 multiple times and add those
                    crossings = 1 + (move_by - starting_point) // 100
                else:
                    crossings = 0
                starting_point = (starting_point - move_by) % 100

            crossed_0 += crossings

    return crossed_0


print(main())
