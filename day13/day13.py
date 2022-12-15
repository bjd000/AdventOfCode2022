"""
I did what I could on my own, but the recurssion was troubling.  
I disected code from @ramenjunkie@layer8.space until i understood it and recreated it.
Source:  https://bloggingintensifies.com/advent-of-code-2022-day-13/

Fore part two, I would not have got there anytime soon without the functools.cmp_to_key tip.
Reading the documentation and finding some other examples helped.
"""
from enum import Enum
from functools import cmp_to_key


class Order(Enum):
    UNSURE = 0
    GOOD = 1
    BAD = -1


def compare_packets(left: list, right: list):

    if isinstance(left, int) and isinstance(right, int):
        if left < right:
            return Order.GOOD.value
        elif left > right:
            return Order.BAD.value
        else:
            return Order.UNSURE.value

    if isinstance(left, list) and isinstance(right, list):

        for item in range(min(len(left), len(right))):
            condition = compare_packets(left[item], right[item])
            if condition != Order.UNSURE.value:
                return condition

        if len(left) < len(right):
            return Order.GOOD.value
        elif len(left) > len(right):
            return Order.BAD.value

    if isinstance(left, int) and isinstance(right, list):
        return compare_packets([left], right)

    if isinstance(left, list) and isinstance(right, int):
        return compare_packets(left, [right])

    return Order.UNSURE.value


def main(file: str) -> None:
    with open(file, "r") as f:
        pkt_grps = [list(map(eval, l.split("\n"))) for l in f.read().split("\n\n")]

    packet_indicies: list = []
    packet_index = 0
    ordered_packets = []  # part 2

    for packets in pkt_grps:
        packet_index += 1
        if compare_packets(left=packets[0], right=packets[1]) == Order.GOOD.value:
            packet_indicies.append(packet_index)
        ordered_packets.append(packets[0])  # part 2
        ordered_packets.append(packets[1])  # part 2

    print(sum(packet_indicies))  # Part 1 asnwer = 4894

    # Part 2
    ordered_packets.append([[2]])
    ordered_packets.append([[6]])
    ordered_packets.sort(key=cmp_to_key(compare_packets), reverse=True)
    print((ordered_packets.index([[2]]) + 1) * (ordered_packets.index([[6]]) + 1))


if __name__ == "__main__":
    main("data/input.txt")
