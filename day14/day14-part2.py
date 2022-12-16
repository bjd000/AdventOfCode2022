def parse_data(file: str) -> set:

    with open(file) as f:
        rocklines = [list(l.split(" -> ")) for l in f.read().split("\n")]

    cols: set = set()
    rows: set = set()
    rock_loc: set = set()

    for j, rocks in enumerate(rocklines):
        # sample rocks: ['498,4', '498,6', '496,6']
        line_beg: list = []
        line_end: list = []

        for i, xy in enumerate(rocks):

            col: int = int(xy.split(",")[0])
            row: int = int(xy.split(",")[1])
            cols.add(col)  # unique set of all col (x) values
            rows.add(row)  # unique set of all row (y) values

            if i == 0:
                line_beg = [col, row]
            else:
                line_end = [col, row]

            if line_beg and line_end:  # if both have values
                rock_loc.update(locate_rocks(line_beg, line_end))
                line_beg = [col, row]

    return cols, rows, rock_loc


def create_matrix(max_col: int, min_col: int, max_row: int) -> list:

    matrix: list = []
    empty_row: list = []
    floor: list = []

    for i in range(0, max_col * 2):
        empty_row.append(".")
        floor.append("#")

    for j in range(0, max_row + 2):
        matrix.append(empty_row.copy())

    matrix.append(floor)

    return matrix


def display_matrix(matrix: list) -> None:

    for i, val in enumerate(matrix):
        print(f"{i:3}", "".join(val[400:600]))


def locate_rocks(begin: list, end: list) -> list:

    # print(f"start: {begin}, end: {end} - ", end="")
    rocks: list = []

    # beg and end x values the same = vertical line
    if begin[0] == end[0]:
        # print("vertical - ", end="")

        for i in range(abs(end[1] - begin[1]) + 1):
            # assumes we don't ever get an entry like 489:5, 489:5 - no single rocks
            lowest_row: int = begin[1] if (begin[1] < end[1]) else end[1]
            rocks.append((begin[0], lowest_row + i))

    # beg and end y values the same = horizonatal
    else:
        # print("horizontal - ", end="")

        for i in range(abs(end[0] - begin[0]) + 1):
            lowest_col: int = begin[0] if (begin[0] < end[0]) else end[0]
            rocks.append((lowest_col + i, begin[1]))

    # print(rocks)
    return rocks


def load_rocks(rock_set: set, cave: list) -> None:

    cave[0][500] = "+"

    for rock in rock_set:
        row = rock[1]
        col = rock[0]
        cave[row][col] = "#"


def drop_sand(cave: list) -> int:

    sand_units: int = 0
    moves_remaining: bool = True
    drop_col: int = 500

    while moves_remaining:

        sand_xy: list = [0, drop_col]  # sand staring position
        drop = True

        while drop:
            if sand_xy[0] > len(cave) - 1:
                moves_remaining = False
                drop = False
            elif cave[sand_xy[0] + 1][sand_xy[1]] == ".":
                sand_xy[0] += 1
            elif cave[sand_xy[0] + 1][sand_xy[1] - 1] == ".":
                sand_xy[0] += 1
                sand_xy[1] -= 1
            elif cave[sand_xy[0] + 1][sand_xy[1] + 1] == ".":
                sand_xy[0] += 1
                sand_xy[1] += 1
            else:
                if sand_xy == [0, drop_col]:
                    moves_remaining = False
                else:
                    cave[sand_xy[0]][sand_xy[1]] = "O"
                sand_units += 1
                drop = False

    return sand_units


def main(file: str) -> None:

    cols: set = set()  # unique set of all col (x) values
    rows: set = set()  # unique set of all row (y) values
    rock_loc: set = set()  # (x,y) locations for all rocks
    cave: list = []
    cave_cols: list = []

    cols, rows, rock_loc = parse_data(file)

    cave = create_matrix(max(cols), min(cols), max(rows))
    # display_matrix(cave) # empty matrix

    load_rocks(rock_loc, cave)
    # display_matrix(cave)  # cave matrix with rocks

    ### PART 2 ###
    print(f"Units of Sand = {drop_sand(cave)}")  # 24,377 Correct Answer
    # display_matrix(cave)


if __name__ == "__main__":
    main("data/input.txt")
