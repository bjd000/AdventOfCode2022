def find_marker(datastream: str, min_diff: int) -> int:
    reg_list: list = []
    for i, char in enumerate(datastream):

        if len(reg_list) == min_diff:
            reg_list.pop(0)
        reg_list.append(char)

        if len(set(reg_list)) == min_diff:
            return i + 1


def main(file: str) -> None:

    with open(file, "r") as f:
        line = f.read()

    print(find_marker(line, 4))
    print(find_marker(line, 14))


if __name__ == "__main__":
    main("data/input.txt")
