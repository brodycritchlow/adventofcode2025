import enum
from grab_input import grab_input

grab_input("https://adventofcode.com/2025/day/4/input")


def main():
    grid = []
    count = 0
    non_open_slots = 0
    direction_keys = (
        "north",
        "south",
        "west",
        "east",
        "northwest",
        "northeast",
        "southwest",
        "southeast",
    )
    directions = {
        "north": (0, 1),
        "south": (0, -1),
        "west": (-1, 0),
        "east": (1, 0),
        "northwest": (-1, 1),
        "northeast": (1, 1),
        "southwest": (-1, -1),
        "southeast": (1, -1),
    }

    with open("input.txt", "r") as f:
        for line in f.readlines():
            line = line.strip()
            grid.append([char for char in line])

        for row_idx, row in enumerate(grid):
            for col_idx, col in enumerate(row):
                if col != "@":
                    continue
                non_open_slots = 0
                for direction in direction_keys:
                    change = directions[direction]

                    new_row = row_idx + change[1]
                    new_col = col_idx + change[0]

                    if 0 <= new_row < len(grid) and 0 <= new_col < len(grid[0]):
                        space = grid[new_row][new_col]
                        if space == "@":
                            non_open_slots += 1
                if non_open_slots < 4:
                    count += 1

    return count


if __name__ == "__main__":
    print(main())
