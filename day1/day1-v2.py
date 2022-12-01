"""Playing with classes.  Overkill, but good for learning."""


class ElfCalories:
    def __init__(self, file: str) -> None:
        with open(file, "r") as f:
            self.calorie_data: list = f.read().split("\n\n")
        self.calorie_totals: list[int] = self._create_totals_list()

    def _create_totals_list(self) -> list:
        totals_list: list = []
        i: int = 0
        while i < len(self.calorie_data):
            calorie_subset: list = self.calorie_data[i].split("\n")
            sum: int = 0
            for calories in calorie_subset:
                sum += int(calories)
            totals_list.append(sum)
            i += 1
        return totals_list

    def find_top_hoarder(self) -> None:
        max_cal = max(self.calorie_totals)
        print(f"The elf with the most has {max_cal} combined calories.")
        return

    def find_top_n(self, num: int) -> None:
        self.calorie_totals.sort()
        top_n: list[int] = self.calorie_totals[-num:]
        print(f"The top {num} elves have {sum(top_n)} calories.")


def main() -> None:
    elf_food = ElfCalories("day1-input.txt")
    elf_food.find_top_hoarder()
    elf_food.find_top_n(3)


if __name__ == "__main__":
    main()
