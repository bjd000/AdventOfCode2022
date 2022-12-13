"""
I had the class and game logic correct.  Needed help with part two.  I learned a lot from looking
at this website:

https://chasingdings.com/2022/12/11/advent-of-code-day-11-monkey-in-the-middle/

I changed the way I was parsing my data a little, but the eval and lambda's in the class were the
big take aways.  And the return funcction/lambda in the play_a_game function, even though I did
it without the lambda.  I finally understood it, but left my code as it was easier for me to 
understand.
"""


class Monkey:
    def __init__(self, monkey_data: list) -> object:
        monkey_details = monkey_data.splitlines()
        self.items = eval("[" + monkey_details[1][18:] + "]")
        self.operation = eval("lambda old:" + monkey_details[2][19:])
        self.test = int(monkey_details[3][21:])
        self.iftrue = int(monkey_details[4][29:])
        self.iffalse = int(monkey_details[5][30:])
        self.inspections = 0

    def take_turn(self, monkeys: list, worry_div: int):
        while self.items:
            self.inspections += 1
            # calc worry level after inspection

            worry_level = self.operation(self.items.pop(0))
            if worry_div == 1:
                worry_level = worry_level % 9_699_690
            else:
                worry_level = worry_level // worry_div
            # test to determine which monkey receives the item
            if worry_level % self.test == 0:
                monkeys[self.iftrue].items.append(worry_level)
            else:
                monkeys[self.iffalse].items.append(worry_level)


def play_game(file: str, game_rounds: int, worry_div: int) -> int:

    # parse input & create list of monkey objects
    with open(file, "r") as f:
        monkeys = [Monkey(monkey_data) for monkey_data in f.read().split("\n\n")]

    for _ in range(game_rounds):
        for monkey in monkeys:
            monkey.take_turn(monkeys, worry_div)

    x, y = sorted([monkey.inspections for monkey in monkeys])[-2:]
    return x * y  # 64032 is correct answer


def main(file: str) -> None:

    part1 = play_game(file, 20, 3)
    print("Part 1 = ", part1)  # 64032 is correct answer

    part2 = play_game(file, 10000, 1)
    print("Part 2 = ", part2)  # 12729522272 is correct answer


if __name__ == "__main__":
    main("data/input.txt")
