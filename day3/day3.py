# https://adventofcode.com/2022/day/3

"""Started off with functions for part 1, then just crammed part to into Main.
I would like to make the  compare_compartments function useful for comapring any
number of passed arguments, but I need to figure out the logic.

Also might be able to adjust it so you don't have to iterate over the rucksacks list twice.
"""


def create_priority_lookup() -> dict:
    """Create and return a dictionary that maps alphas to pre-determined integers."""

    alphabet_lower: dict[str, int] = {}
    alphabet_upper: dict[str, int] = {}
    priority_lower: int = 1
    priority_upper: int = 27

    for i in range(97, 123):
        alphabet_lower[chr(i)] = priority_lower
        priority_lower += 1

    for i in range(65, 91):
        alphabet_upper[chr(i)] = priority_upper
        priority_upper += 1

    return {**alphabet_lower, **alphabet_upper}


def split_rucksacks(ruck: str) -> tuple[str, str]:
    """Split the ruck into two compartments and return them in a tuple."""

    half: int = int(len(ruck) / 2)
    compartment_one = ruck[half:]
    compartment_two = ruck[:half]

    return (compartment_one, compartment_two)


def compare_compartments(compartments: tuple) -> str:
    """Compare the compartments in the tuple and reutrn the item that is in both."""

    item_in_both = "".join(set(compartments[0]) & set(compartments[1]))
    return item_in_both


def main(file: str):

    with open(file, "r") as f:
        rucksacks = f.read().split("\n")

    priorities: dict[str, int] = create_priority_lookup()
    priority_sum: int = 0

    for ruck in rucksacks:

        compartments: tuple[str, str] = split_rucksacks(ruck)
        unique_item: str = compare_compartments(compartments)
        item_priority: int = priorities[unique_item]
        priority_sum += item_priority

    print(f"Part 1: The sum of priorities = {priority_sum}")

    rucks_evaluated: int = 0
    ruck_start: int = 0
    ruck_stop: int = 3
    ruck_interval: int = 3
    badge_priority_sum: int = 0
    while rucks_evaluated < len(rucksacks):
        ruck_group: tuple(list, list, list) = ()
        ruck_group = rucksacks[ruck_start:ruck_stop]
        badge: str = "".join(
            set(ruck_group[0]) & set(ruck_group[1]) & set(ruck_group[2])
        )
        badge_priority_sum += priorities[badge]
        ruck_start += ruck_interval
        ruck_stop += ruck_interval
        rucks_evaluated += ruck_interval

    print(f"Part 2: The sum of badge priorities = {badge_priority_sum}")


if __name__ == "__main__":
    main("input.txt")
