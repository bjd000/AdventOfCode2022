# https://adventofcode.com/2022/day/3


def get_priority(letter: str) -> int:

    priority: int = 0

    if letter.isupper():
        priority = (ord(letter) - ord("A")) + 27
    else:
        priority = (ord(letter) - ord("a")) + 1

    return priority


def split_input(ruck: str) -> set:

    half: int = int(len(ruck) / 2)
    set1: set = set(ruck[half:])
    set2: set = set(ruck[:half])

    return set1, set2


def solve_part1(rucksacks: list) -> None:

    priority_sum: int = 0

    for ruck in rucksacks:

        compartment1, compartment2 = split_input(ruck)
        common_item: str = "".join(compartment1.intersection(compartment2))
        priority_sum += get_priority(common_item)

    print(f"Part 1: The sum of priorities = {priority_sum}")


def solve_part2(rucksacks: list) -> None:

    priority_sum: int = 0

    for i in range(0, len(rucksacks), 3):
        ruck1 = set(rucksacks[i])
        ruck2 = set(rucksacks[i + 1])
        ruck3 = set(rucksacks[i + 2])
        common_item: str = "".join(ruck1.intersection(ruck2).intersection(ruck3))
        priority_sum += get_priority(common_item)

    print(f"Part 2: The sum of badge priorities = {priority_sum}")


def main(file: str):

    with open(file, "r") as f:
        rucksacks = f.read().split("\n")

    solve_part1(rucksacks)
    solve_part2(rucksacks)


if __name__ == "__main__":
    main("input.txt")
