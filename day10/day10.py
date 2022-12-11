def check_signal(cycle: int, reg: int):
    signal = 0
    if cycle in (20, 60, 100, 140, 180, 220):
        signal = cycle * reg
    return signal


def update_crt_loc(crt_loc: list) -> None:
    if crt_loc[1] + 1 > 39:
        crt_loc[0] += 1
        crt_loc[1] = 0
    else:
        crt_loc[1] += 1


def crt_write(crt_loc: list, sprite_loc: list, display: list):
    if crt_loc[1] in sprite_loc:
        display[crt_loc[0] - 1].append("#")
    else:
        display[crt_loc[0] - 1].append(".")


def update_sprite_loc(sprite_loc, register):
    sprite_loc[0] = register - 1
    sprite_loc[1] = register
    sprite_loc[2] = register + 1


def main(file: str):

    with open(file, "r") as f:
        signals: list = f.read().split("\n")

    register: int = 1
    cycle: int = 0
    strength: list = []
    crt_loc: list = [1, 0]  # row, line position
    sprite_loc: list = [0, 1, 2]
    display = [[], [], [], [], [], [], []]

    for signal in signals:
        if signal.startswith("noop"):

            crt_write(crt_loc, sprite_loc, display)
            update_crt_loc(crt_loc)
            cycle += 1
            strength.append(check_signal(cycle, register))

        else:
            # first clock cycle
            crt_write(crt_loc, sprite_loc, display)
            update_crt_loc(crt_loc)
            cycle += 1
            strength.append(check_signal(cycle, register))
            reg_inc = int(list(signal.split(" "))[1])

            # second clock cycle
            crt_write(crt_loc, sprite_loc, display)
            update_crt_loc(crt_loc)
            cycle += 1
            strength.append(check_signal(cycle, register))
            register += reg_inc

            update_sprite_loc(sprite_loc, register)

    # part one
    print(sum(strength))

    # part two
    for lst in display:
        print("".join(lst))


if __name__ == "__main__":
    main("data/input.txt")
