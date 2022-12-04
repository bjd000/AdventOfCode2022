def find_range(delimiters: str) -> range:

    start, stop = delimiters.split("-")
    r = set(range(int(start), int(stop) + 1))
    return r


def main(file: str) -> None:

    with open(file, "r") as f:
        assignments = f.read().split("\n")

    full_overlap_cnt: int = 0
    part_overlap_cnt: int = 0

    for pair_of_assigments in assignments:
        assignment1, assignment2 = pair_of_assigments.split(",")
        sections1 = set(find_range(assignment1))
        sections2 = set(find_range(assignment2))

        # Full overlap/inclusion check
        if sections1 == sections2:
            full_overlap_cnt += 1
        elif sections1.issubset(sections2) or sections2.issubset(sections1):
            full_overlap_cnt += 1

        # Partial overlap check
        if len(sections1.intersection(sections2)) > 0:
            part_overlap_cnt += 1

    print(f"Assignment pairs which contain another range = {full_overlap_cnt}")
    print(f"Assignment pairs with any overlap = {part_overlap_cnt}")


if __name__ == "__main__":
    main("input.txt")
