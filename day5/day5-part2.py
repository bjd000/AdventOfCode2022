"""In my first attempt I did not parse the stack layout for the input file."""

import re

# Starting Stack Layout
STACK_MAP = {
    "1": ["L", "N", "W", "T", "D"],
    "2": ["C", "P", "H"],
    "3": ["W", "P", "H", "N", "D", "G", "M", "J"],
    "4": ["C", "W", "S", "N", "T", "Q", "L"],
    "5": ["P", "H", "C", "N"],
    "6": ["T", "H", "N", "D", "M", "W", "Q", "B"],
    "7": ["M", "B", "R", "J", "G", "S", "L"],
    "8": ["Z", "N", "W", "G", "V", "B", "R", "T"],
    "9": ["W", "G", "D", "N", "P", "L"],
}


def move_crates(qty: int, start: str, end: str) -> None:

    crates: list = []

    for i in range(qty):
        crates.append(STACK_MAP[start].pop())

    crates.reverse()
    STACK_MAP[end] += crates


def find_top_crates() -> str:
    top_crates: str = ""

    for stack in STACK_MAP.values():
        top_crates += stack[-1]

    return top_crates


def main(file: str) -> None:

    pattern = re.compile(r"\d+")

    with open(file, "r") as f:
        crate_moves = f.read().split("\n")

    for move in crate_moves:
        coordinates = pattern.findall(move)
        move_crates(int(coordinates[0]), str(coordinates[1]), str(coordinates[2]))

    print(f"Top Crates in the Stacks: {find_top_crates()}")


if __name__ == "__main__":
    main("input-wo-stacks.txt")
