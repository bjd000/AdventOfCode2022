"""Final version includes parsing the whole input file."""

import re
from copy import deepcopy


def parse_input(file: str) -> tuple[list, list]:

    with open(file, "r") as f:
        lines: list = f.read().split("\n")

    stack_lines: list = []
    moves: list = []
    pattern = re.compile(r"\d+")

    for line in lines:
        if line == "":
            continue

        if line.startswith("move"):
            matches = pattern.findall(line)
            move = {
                "qty": int(matches[0]),
                "from": int(matches[1]),
                "to": int(matches[2]),
            }
            moves.append(move)
        else:
            stack_lines.append(line)

    # Get rid of stack title row
    stack_lines.pop()

    return stack_lines, moves


def parse_stack_data(stack_lines: list) -> dict:

    stacks: dict = {}
    pattern: str = re.compile("(?:\[(.)\ ?]|    ?)")

    for line in reversed(stack_lines):
        crates: list = pattern.findall(line)

        for i, crate in enumerate(crates):

            # Create stack key if it does not exist
            if stacks.get(i + 1) == None:
                stacks[i + 1] = []

            # Add value (crate) to correct stack key if value was found
            if crate != "":
                stacks[i + 1].append(crate)

    return stacks


def move_crates_part1(stacks: dict, qty: int, start: int, end: int) -> None:

    for i in range(qty):
        crate: str = stacks[start].pop()
        stacks[end].append(crate)


def move_crates_part2(stacks: dict, qty: int, start: int, end: int) -> None:

    crates: list = []

    for i in range(qty):
        crates.append(stacks[start].pop())

    crates.reverse()
    stacks[end] += crates


def find_top_crates(stacks: dict) -> str:
    top_crates: str = ""

    for stack in stacks.values():
        top_crates += stack[-1]

    return top_crates


def part1(moves: list, stacks1: list) -> str:
    for move in moves:
        move_crates_part1(stacks1, int(move["qty"]), int(move["from"]), int(move["to"]))

    return find_top_crates(stacks1)


def part2(moves: list, stacks2: list) -> str:
    for move in moves:
        move_crates_part2(stacks2, int(move["qty"]), int(move["from"]), int(move["to"]))

    return find_top_crates(stacks2)


def main(file: str) -> None:

    stack_lines, moves = parse_input(file)
    stacks = parse_stack_data(stack_lines)
    stacks1 = deepcopy(stacks)
    stacks2 = deepcopy(stacks)
    print(f"Part1: Top Crates in the Stacks: {part1(moves, stacks1)}")
    print(f"Part2: Top Crates in the Stacks: {part2(moves, stacks2)}")


if __name__ == "__main__":
    main("input.txt")
